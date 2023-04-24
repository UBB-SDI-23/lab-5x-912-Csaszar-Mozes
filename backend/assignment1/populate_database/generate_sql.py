from generate_pc import generate as generate_pcs
from generate_people import generate as generate_ps
from generate_companies import generate as generate_cs
from generate_locations import generate as generate_ls


def generate_all(nr_people=3000000, nr_companies=1000000, version="Lite"):
    chances = [0.9, 0.097, 0.0027, 0.000297, 0.000003]
    chances_added = [0]
    for i in range(len(chances)):
        chances_added.append(chances_added[i] + chances[i])
    chances_added.append(1)
    nr_people_in_comp = [1, 15, 45, 180, 455, 1300]
    nr_locations_in_comp = [1, 2, 4, 10, 25, 100]
    net_values = [100, 1000, 15764, 547895, 7845962, 54687514]
    salaries = [100, 250, 2500, 25000, 180000, 600000]
    reputations = [20, 60, 70, 80, 90, 100]

    generate_cs(nr_companies, chances_added, reputations, net_values, version)
    generate_ps(nr_people, version)
    generate_ls(chances_added, nr_locations_in_comp, nr_companies, version)
    generate_pcs(chances_added, salaries, nr_people_in_comp, nr_people, nr_companies, version)


generate_all(1000000, 1000000)






































# import faker as fk
# import random as rnd
#
# ## Generate people
#
# BATCH_SIZE = 1000
# fake = fk.Faker()
#
#
# def escape_hypen(string):
#     new_str = ''
#     for let in string:
#         if let == "'":
#             new_str += "''"
#         else:
#             new_str += let
#     return new_str
#
#
#
#
# def generate_location():
#     country = escape_hypen(fake.country())
#     city = escape_hypen(fake.city())
#     street = escape_hypen(fake.street_name())
#     apartment = str(rnd.randint(1, 10000)) if rnd.random() < 0.5 else ""
#     number = str(rnd.randint(1,10000))
#     description = escape_hypen(fake.paragraph(nb_words=10, nb_sentences=10))
#     return "('" + country + "','" + city + "','" + street + "','" + apartment + "'," + number + ",'" + description + "',"
#
# def change_location_to_company(location, company):
#     return location + str(company) + ")"
#
#
#
#
# def generate_pc(p_id, c_id, salary):
#     role = escape_hypen(fake.job())
#     return "('" + role + "'," + str(salary) + "," + str(p_id) + "," + str(c_id) + ")"
#
#
# def generate_all(nr_rows):
#     def write_reset(file, name, schema):
#         file.write('DELETE FROM ' + name + ';\n')
#         file.write("DELETE FROM SQLITE_SEQUENCE WHERE NAME = '" + name + "';\n")
#         #write_insert(file, name, schema)
#
#     def write_insert(file, name, schema):
#         file.write('INSERT INTO ' + name + ' ' + schema + ' VALUES ')
#
#     def write_element(file, row, row_id, name, schema, do_write_insert=True):
#         if (row_id - 1) % BATCH_SIZE == 0:
#             file.write(';\n')
#             if do_write_insert:
#                 write_insert(file, name, schema)
#         else:
#             file.write(',')
#         file.write(row)
#
#
#
#     max_dict_size = 1000
#     # entry = [entity,nr_uses_left, id]
#     cached_people = []
#     # entry = [entity,nr_uses_left]
#     cached_locations = []
#     # entry = id:True
#     used_locations = {}
#     used_people = {}
#     loc_id = 0
#     person_id = 0
#     pc_id = 0
#     worker_id = rnd.randint(1265,16498)
#     schemas = [
#         "(role,salary,person_id,company_id)",
#         "(first_name,last_name,worker_id,email,age)",
#         "(country,city,street,apartment,number,description,company_id)",
#         "(name,description,net_value,reputation,start_year)"
#     ]
#     names = ['a1_api_personworkingatcompany','a1_api_person', 'a1_api_location', 'a1_api_company']
#     files = [
#         open('insert_pc.sql', 'w'), open('insert_p.sql', 'w'), open('insert_l.sql', 'w'), open('insert_c.sql', 'w')
#     ]
#     for i in range(len(files)):
#         write_reset(files[i], names[i], schemas[i])
#     for comp_id in range(1, nr_rows + 1):
#         if comp_id % BATCH_SIZE == 0:
#             print("Batch",comp_id // BATCH_SIZE,"done.")
#         used_locations = {}
#         used_people = {}
#         comp_chance = rnd.random()
#         comp_i = 0
#         while chances_added[comp_i] < comp_chance:
#             comp_i += 1
#         reputation = rnd.randint(reputations[comp_i - 1], reputations[comp_i])
#         net_value = rnd.randint(net_values[comp_i - 1], net_values[comp_i])
#         nr_location = rnd.randint(nr_locations[comp_i - 1], nr_locations[comp_i])
#         nr_person = rnd.randint(nr_people[comp_i - 1], nr_people[comp_i])
#         company = generate_company(net_value, reputation)
#         write_element(files[3], company, comp_id, names[3],schemas[3])
#         for i in range(nr_location):
#             generate = True
#             location = ''
#             #see if you reuse a location or not
#             if rnd.random() < (len(cached_locations) - len(used_locations)) / max_dict_size:
#                 ##choose a location randomly from list
#                 ind = rnd.randint(0, len(cached_locations) - 1)
#                 generate = False
#                 ##if location is already used
#                 if used_locations.get(ind, False):
#                     generate = True
#                 else:
#                     cached_locations[ind][1] = cached_locations[ind][1] - 1
#                     location = change_location_to_company(cached_locations[ind][0], comp_id)
#                     #if the locations number of uses is up, remove it
#                     if cached_locations[ind][1] == 0:
#                         if len(cached_locations) == 1:
#                             cached_locations = []
#                         else:
#                             cached_locations[ind] = cached_locations[len(cached_locations) - 1]
#                             cached_locations.pop()
#                     else:
#                         used_locations[ind] = True
#             if generate:
#                 ##create new location
#                 location = generate_location()
#                 nr_uses = rnd.randint(0, 1)
#                 ##if it can be used more than once
#                 if nr_uses > 0:
#                     ##if there is space for it, just append this to the end
#                     if len(cached_locations) < max_dict_size:
#                         cached_locations.append([location, nr_uses])
#                         used_locations[len(cached_locations) - 1] = False
#                     ##if length is larger than max, randomly substitute one location with this one
#                     else:
#                         ind = rnd.randint(0, max_dict_size-1)
#                         cached_locations[ind] = [location, nr_uses]
#                         used_locations[ind] = False
#                 location = change_location_to_company(location, comp_id)
#             loc_id += 1
#             write_element(files[2], location, loc_id, names[2], schemas[2])
#         for i in range(nr_person):
#             generate = True
#             person = ''
#             p_id = 0
#             #see if you reuse a person or not
#             if rnd.random() < (len(cached_people) - len(used_people)) / max_dict_size:
#                 ##choose a location randomly from list
#                 ind = rnd.randint(0, len(cached_people) - 1)
#                 generate = False
#                 if used_people.get(ind, False):
#                     generate = True
#                 else:
#                     cached_people[ind][1] = cached_people[ind][1] - 1
#                     person = cached_people[ind][0]
#                     p_id = cached_people[ind][2]
#                     #if the people number of uses is up, remove it
#                     if cached_people[ind][1] == 0:
#                         if len(cached_people) == 1:
#                             cached_people = []
#                         else:
#                             used_people[len(cached_people) - 1] = False
#                             cached_people[ind] = cached_people[len(cached_people) - 1]
#                             cached_people.pop()
#                             used_people[ind] = True
#                     else:
#                         used_people[ind] = True
#             if generate:
#                 person_id += 1
#                 ##create new person
#                 person = generate_person(worker_id)
#                 worker_id += rnd.randint(1, 5)
#                 nr_uses = rnd.randint(1, 4)
#                 ##if it can be used more than once
#                 if nr_uses > 0:
#                     ##if there is space for it, just append this to the end
#                     if len(cached_people) < max_dict_size:
#                         cached_people.append([person, nr_uses, person_id])
#                         used_people[len(cached_people) - 1] = True
#                     ##if length is larger than max, randomly substitute one location with this one
#                     else:
#                         ind = rnd.randint(0, max_dict_size-1)
#                         cached_people[ind] = [person, nr_uses, person_id]
#                         used_people[ind] = True
#                 p_id = person_id
#                 write_element(files[1], person, person_id, names[1], schemas[1])
#             salary = rnd.randint(salaries[comp_i - 1], salaries[comp_i])
#             pc = generate_pc(p_id, comp_id, salary)
#             pc_id += 1
#             write_element(files[0], pc, pc_id, names[0], schemas[0])
#     #complete sql file with ;
#     for i in range(len(files)):
#         write_element(files[i], '', 1, names[i], schemas[i], False)
#         files[i].close()
#
#
# for _ in range(10000):
#     if "'" in fake.word():
#         print("HYPEN")
#
#
# #generate_all(1001000)
