import faker as fk
import random as rnd

fake = fk.Faker()


def escape_single_quote(string):
    new_str = ''
    for let in string:
        if let == "'":
            new_str += "''"
        elif let == ",":
            new_str += ""
        else:
            new_str += let
    return new_str


def generate_company(net_value, reputation, nr_users, single_user=None):
    name = escape_single_quote(fake.company())
    description = escape_single_quote(fake.catch_phrase())
    start_year = rnd.randint(1750, 2023)
    user_id = str(rnd.randint(1, nr_users)) if single_user is None else single_user
    return "('" + name + "','" + description + "'," + str(net_value) + "," + str(reputation) + "," + \
           str(start_year) + "," + str(user_id) + ")", name


def change_name_of_company(company, name):
    company = company.split(',')
    company[0] = "('" + escape_single_quote(name) + "'"
    company_r = ''
    for c_part in company:
        company_r += c_part + ','
    return company_r[:-1]


def generate(nr, chances_added, reputations, net_values, nr_users, can_truncate=True, single_user=None, batch_size=1000):
    print("GENERATING COMPANIES")
    file = open('data_generation/insert_c.sql', 'w+')
    if can_truncate:
        file.write('ALTER TABLE a1_api_company DISABLE TRIGGER ALL;TRUNCATE a1_api_company RESTART IDENTITY CASCADE;')

    i_ca = 1
    nr_written = 0
    stmt = 'INSERT INTO a1_api_company (name,description,net_value,reputation,start_year,user_id) VALUES '

    names = {}
    for c_id in range(1, nr + 1):

        # Determine range of reputation to generate for the company
        if c_id > chances_added[i_ca] * nr:
            i_ca += 1

        if nr_written != 0:
            stmt += ","
        reputation = rnd.randint(reputations[i_ca - 1], reputations[i_ca])
        net_value = rnd.randint(net_values[i_ca - 1], net_values[i_ca])

        company, name = generate_company(net_value, reputation, nr_users, single_user)
        if names.get(name) is not None:
            names[name] += 1
            name = name + ' ' + str(names[name])
            company = change_name_of_company(company, name)
        else:
            names[name] = 1
        stmt += company
        nr_written += 1

        # if written more than batch size, write stmt to new line
        if nr_written > batch_size:
            nr_written = 0
            file.write(stmt + ";\n")
            stmt = 'INSERT INTO a1_api_company (name,description,net_value,reputation,start_year,user_id) VALUES '
        if c_id % batch_size == 0:
            print("Finished with " + str(c_id) + " companies!")
    #write out last line as well
    if nr_written != 0:
        file.write(stmt + ";\n")
    file.write('ALTER TABLE auth_user ENABLE TRIGGER ALL;')
    file.close()
