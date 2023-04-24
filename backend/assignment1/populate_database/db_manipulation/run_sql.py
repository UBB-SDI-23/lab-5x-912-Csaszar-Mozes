import sqlite3

# for name in ['insert_p.sql', 'insert_c.sql', 'insert_l.sql', 'insert_pc.sql']:
#     db = sqlite3.connect('../../db.sqlite3')
#     with open('../data_generation/' + name, 'r') as sql_file:
#         command = sql_file.readline()
#         i = 0
#         while command:
#             cursor = db.cursor()
#             try:
#                 cursor.executescript(command)
#             except sqlite3.OperationalError:
#                 print(command)
#             db.commit()
#
#             command = sql_file.readline()
#             i += 1
#             if i % 100 == 0:
#                 print("Finished", i, "command(s).")
#         print(name, "finished successfully.")
#     db.close()
#
# print("Finished inserting.");
#
# #
# db = sqlite3.connect('../../db.sqlite3')
# cursor = db.cursor()
# for name in ['location', 'personworkingatcompany', 'company', 'person']:
#     command = 'SELECT COUNT(*) FROM a1_api_' + name
#     print(name,":",db.execute(command).fetchall())
#
# db.commit()
# db.close()


with open('../db_manipulation/set_up_avg_salary.sql', 'r') as sql_file:
    db = sqlite3.connect('../../db.sqlite3')
    command = sql_file.readline()
    i = 0
    while command:
        cursor = db.cursor()
        try:
            cursor.executescript(command)
        except sqlite3.OperationalError:
            print(command)
        db.commit()

        command = sql_file.readline()
        i += 1
        if i % 100 == 0:
            print("Finished", i, "command(s).")
    print("Updating Avg_Salary finished successfully.")
    db.close()
