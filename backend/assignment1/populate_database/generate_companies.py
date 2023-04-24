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


def generate_company(net_value, reputation):
    name = escape_single_quote(fake.company())
    description = escape_single_quote(fake.catch_phrase())
    start_year = rnd.randint(1750, 2023)
    return "('" + name + "','" + description + "'," + str(net_value) + "," + str(reputation) + "," + str(start_year) + ")", name

def change_name_of_company(company, name):
    company = company.split(',')
    company[0] = "('" + escape_single_quote(name) + "'"
    company_r = ''
    for c_part in company:
        company_r += c_part + ','
    return company_r[:-1]


def generate(nr, chances_added, reputations, net_values, version, batch_size=1000):
    print("GENERATING COMPANIES")
    file = open('data_generation/insert_c.sql', 'w')
    if version == "Lite":
        file.write('DELETE FROM a1_api_company;')
        file.write("DELETE FROM sqlite_sequence WHERE name = 'a1_api_company';")
    else:
        file.write('TRUNCATE a1_api_company RESTART IDENTITY RESTRICT;')

    i_ca = 1
    nr_written = 0
    stmt = 'INSERT INTO a1_api_company (name,description,net_value,reputation,start_year) VALUES '

    names = {}
    for c_id in range(1, nr + 1):

        # Determine range of reputation to generate for the company
        if c_id > chances_added[i_ca] * nr:
            i_ca += 1

        if nr_written != 0:
            stmt += ","
        reputation = rnd.randint(reputations[i_ca - 1], reputations[i_ca])
        net_value = rnd.randint(net_values[i_ca - 1], net_values[i_ca])


        company, name = generate_company(net_value, reputation)
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
            stmt = 'INSERT INTO a1_api_company (name,description,net_value,reputation,start_year) VALUES '
        if c_id % batch_size == 0:
            print("Finished with " + str(c_id) + " companies!")
    #write out last line as well
    if stmt != 'INSERT INTO a1_api_company (name,description,net_value,reputation,start_year) VALUES ':
        file.write(stmt + ";\n")
    file.close()
