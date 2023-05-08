

import faker as fk
import random as rnd
import string

fake = fk.Faker()


def escape_single_quote(stri):
    new_str = ''
    for let in stri:
        if let == "'":
            new_str += "''"
        elif let == ",":
            new_str += ""
        else:
            new_str += let
    return new_str


def change_email_of_user(user, email):
    user = user.split(',')
    user[1] = "'" + email + "'"
    user_r = ''
    for u_part in user:
        user_r += u_part + ','
    return user_r[:-1]


def change_name_of_user(user, name):
    user = user.split(',')
    user[0] = "('" + name + "'"
    user_r = ''
    for u_part in user:
        user_r += u_part + ','
    return user_r[:-1]


def generate_user_profile(user_id, first_name, last_name):
    bio = escape_single_quote(fake.paragraph(nb_sentences=12, variable_nb_sentences=True))
    university = escape_single_quote(fake.sentence(nb_words=7))
    high_school = escape_single_quote(fake.sentence(nb_words=7))
    return "('" + first_name + "','" + last_name + "','" + bio + "','" + university + "','" + high_school + "'," + str(user_id) + ",1,'agesegwsgwaw')"


def generate_username(first_name, last_name):
    first = first_name.lower()[len(first_name) // 2 - 1: len(first_name) // 2 + 2]
    last = last_name.lower()[len(last_name) // 2 - 1: len(last_name) // 2 + 2]
    return first + rnd.choice(string.ascii_lowercase) + last + str(rnd.randint(100, 999))


def generate_user():
    first_name = escape_single_quote(fake.first_name())
    last_name = escape_single_quote(fake.last_name())
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
    username = generate_username(first_name, last_name)
    return username, email, first_name, last_name


def put_user_together(username, email, password):
    return "('" + username + "','" + email + "','" + password + "',true,false,false,'','','2023-04-27 22:18:54')"


def generate(nr, batch_size=1000):
    print("GENERATING USERS AND PROFILES")
    file_u = open('data_generation/insert_u.sql', 'w')
    file_up = open('data_generation/insert_up.sql', 'w')

    file_u.write('ALTER TABLE auth_user DISABLE TRIGGER ALL; TRUNCATE auth_user RESTART IDENTITY CASCADE;\n')
    file_up.write('TRUNCATE a1_api_userprofile RESTART IDENTITY CASCADE; \n')

    # unhashed password = Easy123Pass
    password = 'pbkdf2_sha256$390000$VxXug1jiSC6hHTD9MUAEuJ$qZvuOVv2BToBIcrWKm4+DZ+/6FyZ84pAq0/wDb1MwEM='
    nr_written = 0
    stmt_u = 'INSERT INTO auth_user (username,email,password,is_active,is_staff,is_superuser,first_name,last_name,date_joined) VALUES '
    stmt_up = 'INSERT INTO a1_api_userprofile (first_name,last_name,bio,university,high_school,user_id,role,activation_code) VALUES '
    usernames = {}
    emails = {}
    for i_u in range(1, nr + 1 - 2):
        if nr_written != 0:
            stmt_u += ","
            stmt_up += ","

        name, email, first_name, last_name = generate_user()
        if usernames.get(name) is not None:
            usernames[name] += 1
            name = name + str(usernames[name])
        else:
            usernames[name] = 1
        if emails.get(email) is not None:
            emails[email] += 1
            email = email.split('@')[0] + emails[email] + email.split('@')[1]
        user = put_user_together(name, email, password)
        user_profile = generate_user_profile(i_u, first_name, last_name)

        stmt_u += user
        stmt_up += user_profile
        nr_written += 1

        # if written more than batch size, write stmt to new line
        if nr_written > batch_size:
            nr_written = 0
            file_u.write(stmt_u + ";\n")
            file_up.write(stmt_up + ";\n")
            stmt_u = 'INSERT INTO auth_user (username,email,password,is_active,is_staff,is_superuser,first_name,last_name,date_joined) VALUES '
            stmt_up = 'INSERT INTO a1_api_userprofile (first_name,last_name,bio,university,high_school,user_id, role,activation_code) VALUES '
        if i_u % batch_size == 0:
            print("Finished with " + str(i_u) + " users!")
    #write out last line as well
    if nr_written != 0:
        file_u.write(stmt_u + ";\n")
        file_up.write(stmt_up + ";\n")
    stmt_u = 'INSERT INTO auth_user (username,email,password,is_active,is_staff,is_superuser,first_name,last_name,date_joined) VALUES '
    stmt_up = 'INSERT INTO a1_api_userprofile (first_name,last_name,bio,university,high_school,user_id,role,activation_code) VALUES '
    stmt_u += "('admin','admin@admin.admin','" + password + "',true,true,false,'','','2023-04-27 22:18:54'),"
    stmt_u += "('moderator','moderator@moderator.moderator','" + password + "',false,true,false,'','','2023-04-27 22:18:54');"
    stmt_up += "('Admin','Admin','I''m the admin','',''," + str(nr - 1) + ",3,'sgaszegwvse'),"
    stmt_up += "('Moderator','Moderator','I''m a moderator','',''," + str(nr) + ",2,'wfsegewsgews');"
    file_u.write(stmt_u)
    file_up.write(stmt_up)

    file_u.write('ALTER TABLE auth_user ENABLE TRIGGER ALL;')
    file_u.close()
    file_up.close()
