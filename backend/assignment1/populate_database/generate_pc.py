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


def generate_pc(p_id, c_id, salary):
    role = escape_single_quote(fake.job())
    return "('" + role + "'," + str(salary) + "," + str(p_id) + "," + str(c_id) + ")"


def generate(chances_added, salaries, nr_people_in_comp, nr_people, nr_companies, version, batch_size=1000):
    print("GENERATING PC")

    file = open('data_generation/insert_pc.sql', 'w')
    if version == "Lite":
        file.write('DELETE FROM a1_api_personworkingatcompany;\n')
        file.write("DELETE FROM sqlite_sequence WHERE name = 'a1_api_personworkingatcompany';\n")
    else:
        file.write('TRUNCATE a1_api_personworkingatcompany RESTART IDENTITY RESTRICT;')

    i_ca = 1
    nr_written = 0
    stmt = 'INSERT INTO a1_api_personworkingatcompany (role,salary,person_id,company_id) VALUES '

    for c_id in range(1, nr_companies + 1):

        # Determine range of salary to generate for a person based on company
        if c_id > chances_added[i_ca] * nr_companies:
            i_ca += 1

        # get a random number in the right range of number of people working here
        nr_to_gen = rnd.randint(nr_people_in_comp[i_ca - 1], nr_people_in_comp[i_ca])
        used_people = {}

        for _ in range(nr_to_gen):
            if nr_written != 0:
                stmt += ","
            p_id = rnd.randint(1, nr_people)
            while used_people.get(p_id):
                p_id = rnd.randint(1, nr_people)
            used_people[p_id] = True
            salary = rnd.randint(salaries[i_ca - 1], salaries[i_ca])
            stmt += generate_pc(p_id, c_id, salary)
            nr_written += 1

        # if written more than batch size, write stmt to new line
        if nr_written > batch_size:
            nr_written = 0
            file.write(stmt + ";\n")
            stmt = 'INSERT INTO a1_api_personworkingatcompany (role,salary,person_id,company_id) VALUES '
        if c_id % batch_size == 0:
            print("Finished with " + str(c_id) + " companies!")
        # write out last line as well
    if stmt != 'INSERT INTO a1_api_personworkingatcompany (role,salary,person_id,company_id) VALUES ':
        file.write(stmt + ";\n")
    file.close()
