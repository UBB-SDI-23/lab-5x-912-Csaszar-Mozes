import sqlite3

# for name in ['insert_p.sql', 'insert_c.sql', 'insert_l.sql', 'insert_pc.sql']:
#     with open(name, 'r') as sql_file:
#         command = sql_file.readline()
#         i = 0
#         while command:
#             db = sqlite3.connect('../db.sqlite3')
#             cursor = db.cursor()
#             cursor.executescript(command)
#             db.commit()
#             db.close()
#             command = sql_file.readline()
#             i += 1
#             if i % 100 == 0:
#                 print("Finished",i,"command(s).")
#         print(name, "finished successfully.")
#
# print("Finished inserting.");
#
#
db = sqlite3.connect('../db.sqlite3')
cursor = db.cursor()
for name in ['location', 'personworkingatcompany', 'company', 'person']:
    command = 'SELECT COUNT(*) FROM a1_api_' + name
    print(name,":",db.execute(command).fetchall())

db.commit()
db.close()

#         command = sql_file.readline()
min_val = [100,1000,10000,70000,250000]
max_val = [250, 2500, 25000, 180000, 600000]
rep = [0,60,70,80,90]
# for i in range(5):
#
#     command = f"UPDATE a1_api_personworkingatcompany" \
#               f" SET salary=ABS(RANDOM() % ({max_val[i]} - {min_val[i]} + 1)) + {min_val[i]} " \
#               f"FROM a1_api_company c" \
#               f" WHERE company_id = c.id AND c.reputation>{rep[i]}"
#     db = sqlite3.connect('../db.sqlite3')
#     cursor = db.cursor()
#     cursor.executescript(command)
#     db.commit()
#     db.close()
#     print(command)


for i in range(5):

    command = f"UPDATE a1_api_personworkingatcompany" \
              f" SET salary=floor(random() * ({max_val[i]} - {min_val[i]}) + 1)::int + {min_val[i]} " \
              f"FROM a1_api_company c" \
              f" WHERE company_id = c.id AND c.reputation>{rep[i]};"
    print(command)