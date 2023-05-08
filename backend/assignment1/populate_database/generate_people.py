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


def generate_person(worker_id, nr_users, single_user=None):
    first_name = escape_single_quote(fake.first_name())
    last_name = escape_single_quote(fake.last_name())
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
    age = rnd.randint(18, 100)
    user_id = str(rnd.randint(1, nr_users)) if single_user is None else single_user
    return "('" + first_name + "','" + last_name + "'," + str(worker_id) + ",'" + email + "'," \
           + str(age) + "," + str(user_id) + ")", email


def change_email_of_person(person, email):
    person = person.split(',')
    person[3] = "'" + email + "'"
    person_r = ''
    for p_part in person:
        person_r += p_part + ','
    return person_r[:-1]


def generate(nr, nr_users, can_truncate=True, single_user=None, batch_size=1000):
    print("GENERATING PEOPLE")
    file = open('data_generation/insert_p.sql', 'w')
    if can_truncate:
        file.write('ALTER TABLE a1_api_person DISABLE TRIGGER ALL;\n')
        file.write('TRUNCATE a1_api_person RESTART IDENTITY CASCADE;')
    emails = {}
    worker_id = rnd.randint(1035, 134532)
    for b in range(nr // batch_size):
        stmt = 'INSERT INTO a1_api_person (first_name,last_name,worker_id,email,age,user_id) VALUES '
        for i in range(batch_size):
            if i != 0:
                stmt += ","
            person, email = generate_person(worker_id, nr_users, single_user)
            if emails.get(email) is not None:
                emails[email] += 1
                old_nr = emails[email]
                email = email.split('@')
                email = email[0] + str(old_nr) + "@" + email[1]
                person = change_email_of_person(person, email)
            else:
                emails[email] = 1
            stmt += person
            worker_id += rnd.randint(1, 4)
        file.write(stmt + ";\n")
        print("Finished " + str(b * batch_size) + " with people!")
    stmt = 'INSERT INTO a1_api_person (first_name,last_name,worker_id,email,age,user_id) VALUES '
    for i in range(nr % batch_size):
        if i != 0:
            stmt += ","
        person, email = generate_person(worker_id, nr_users, single_user)
        if emails.get(email) is not None:
            emails[email] += 1
            old_nr = emails[email]
            email = email.split('@')
            email = email[0] + str(old_nr) + "@" + email[1]
            person = change_email_of_person(person, email)
        else:
            emails[email] = 1
        stmt += person
        worker_id += rnd.randint(1, 4)
    file.write(stmt + ";\n")
    file.write('ALTER TABLE a1_api_person ENABLE TRIGGER ALL;')
    file.close()

