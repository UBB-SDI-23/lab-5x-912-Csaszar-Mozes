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


def generate_p_id(nr_users, c_id, nr_people):
    # Get the user id
    u_id = c_id % nr_users
    # Generate a random offset
    rand = rnd.randint(0, nr_people // nr_users) * nr_users
    # If we overshot the number of people, reduce the random offset
    if u_id + rand > nr_people:
        rand -= nr_users
    return u_id + rand


def generate_pc(p_id, c_id, salary, nr_users, single_user=None):
    role = escape_single_quote(fake.job())
    user_id = str(rnd.randint(1, nr_users)) if single_user is None else single_user
    return "('" + role + "'," + str(salary) + "," + str(p_id) + "," + str(c_id) + "," + str(user_id) + ")"


def generate(chances_added, salaries, nr_people_in_comp, nr_users, p_id_range, c_id_range,
             can_truncate=True, single_user=None, batch_size=1000):
    print("GENERATING PC")

    file = open('data_generation/insert_pc.sql', 'w')

    if can_truncate:
        file.write('ALTER TABLE a1_api_personworkingatcompany DISABLE TRIGGER ALL;\n')
        file.write('TRUNCATE a1_api_personworkingatcompany RESTART IDENTITY RESTRICT;')
    i_ca = 1
    nr_written = 0
    stmt = 'INSERT INTO a1_api_personworkingatcompany (role,salary,person_id,company_id, user_id) VALUES '

    for c_id in range(c_id_range[0], c_id_range[1] + 1):

        # Determine range of salary to generate for a person based on company
        if c_id - c_id_range[0] > chances_added[i_ca] * (c_id_range[1] - c_id_range[0] + 1):
            i_ca += 1

        # get a random number in the right range of number of people working here
        nr_to_gen = rnd.randint(nr_people_in_comp[i_ca - 1], nr_people_in_comp[i_ca])
        used_people = {}

        for _ in range(nr_to_gen):
            if nr_written != 0:
                stmt += ","
            p_id = rnd.randint(p_id_range[0], p_id_range[0])
            while used_people.get(p_id):
                p_id = rnd.randint(1, p_id_range[0])
            used_people[p_id] = True
            salary = rnd.randint(salaries[i_ca - 1], salaries[i_ca])
            stmt += generate_pc(p_id, c_id, salary, nr_users, single_user)
            nr_written += 1

        # if written more than batch size, write stmt to new line
        if nr_written > batch_size:
            nr_written = 0
            file.write(stmt + ";\n")
            stmt = 'INSERT INTO a1_api_personworkingatcompany (role,salary,person_id,company_id, user_id) VALUES '
        if c_id % batch_size == 0:
            print("Finished with " + str(c_id) + " companies!")
        # write out last line as well
    if nr_written != 0:
        file.write(stmt + ";\n")
    file.write('ALTER TABLE a1_api_personworkingatcompany ENABLE TRIGGER ALL;')
    file.close()
