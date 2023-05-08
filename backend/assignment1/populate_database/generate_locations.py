import faker as fk
import random as rnd

fake = fk.Faker()


def escape_single_quote(string):
    new_str = ''
    for let in string:
        if let == "'":
            new_str += "''"
        else:
            new_str += let
    return new_str


def generate_location(company_id):
    country = escape_single_quote(fake.country())
    city = escape_single_quote(fake.city())
    street = escape_single_quote(fake.street_name())
    apartment = str(rnd.randint(1, 10000)) if rnd.random() < 0.5 else ""
    number = str(rnd.randint(1,10000))
    description = escape_single_quote(fake.paragraph(nb_sentences=10, variable_nb_sentences=True))
    return "('" + country + "','" + city + "','" + street + "','" + apartment + "'," + number + ",'" + description\
        + "'," + str(company_id) + ")"


def generate(chances_added, nr_locations_in_comp, nr_companies, batch_size=1000):
    print("GENERATING LOCATIONS")

    file = open('data_generation/insert_l.sql', 'w')
    file.write('ALTER TABLE a1_api_location DISABLE TRIGGER ALL; TRUNCATE a1_api_location RESTART IDENTITY RESTRICT;')

    i_ca = 1
    nr_written = 0
    stmt = 'INSERT INTO a1_api_location (country,city,street,apartment,number,description,company_id) VALUES '
    for c_id in range(1, nr_companies + 1):

        # Determine range of number of locations to generate for a company
        if c_id > chances_added[i_ca] * nr_companies:
            i_ca += 1

        #get a random number in the right range of number of locations for current company
        nr_to_gen = rnd.randint(nr_locations_in_comp[i_ca - 1], nr_locations_in_comp[i_ca])
        #generate the number of companies needed
        for _ in range(nr_to_gen):
            if nr_written != 0:
                stmt += ","
            stmt += generate_location(c_id)
            nr_written += 1

        # if written more than batch size, write stmt to new line
        if nr_written > batch_size:
            nr_written = 0
            file.write(stmt + ";\n")
            stmt = 'INSERT INTO a1_api_location (country,city,street,apartment,number,description,company_id) VALUES '
        if c_id % batch_size == 0:
            print("Finished with " + str(c_id) + " companies!")
    if nr_written != 0:
        file.write(stmt + ";\n")
    file.write('ALTER TABLE a1_api_personworkingatcompany ENABLE TRIGGER ALL;')
    file.close()
