import faker as fk
import random as rnd

## Generate people

BATCH_SIZE = 1000
fake = fk.Faker()

def escape_hypen(string):
    new_str = ''
    for let in string:
        if let == "'":
            new_str += "''"
        else:
            new_str += let
    return new_str

def generate_location():
    country = escape_hypen(fake.country())
    city = escape_hypen(fake.city())
    street = escape_hypen(fake.street_name())
    apartment = str(rnd.randint(1, 10000)) if rnd.random() < 0.5 else ""
    number = str(rnd.randint(1,10000))
    description = escape_hypen(fake.paragraph(nb_sentences=10, variable_nb_sentences=True))
    return "('" + country + "','" + city + "','" + street + "','" + apartment + "'," + number + ",'" + description + "'," + str(rnd.randint(1,1000000)) + ")"

def generate(nr):
    file = open('insert_l2.sql', 'w')
    file.write('TRUNCATE a1_api_location RESTART IDENTITY RESTRICT;')
    for b in range(nr // BATCH_SIZE):
        stmt = 'INSERT INTO a1_api_location (country,city,street,apartment,number,description,company_id) VALUES '
        for i in range(BATCH_SIZE):
            if i != 0:
                stmt += ","
            stmt += generate_location()
        file.write(stmt + ";\n")
        print("Finished " + b * BATCH_SIZE)
    file.close()

generate(1003000)