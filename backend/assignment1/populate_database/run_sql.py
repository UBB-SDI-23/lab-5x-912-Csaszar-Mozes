import sqlite3

for name in ['insert_p.sql', 'insert_c.sql', 'insert_l.sql', 'insert_pc.sql']:
    with open(name, 'r') as sql_file:
        command = sql_file.readline()
        i = 0
        while command:
            db = sqlite3.connect('../db.sqlite3')
            cursor = db.cursor()
            cursor.executescript(command)
            db.commit()
            db.close()
            command = sql_file.readline()
            i += 1
            if i % 100 == 0:
                print("Finished",i,"command(s).")
        print(name, "finished successfully.")

print("Finished inserting.");


db = sqlite3.connect('../db.sqlite3')
cursor = db.cursor()
for name in ['location', 'personworkingatcompany', 'company', 'person']:
    command = 'SELECT COUNT(*) FROM a1_api_' + name
    print(name,":",db.execute(command).fetchall())

db.commit()
db.close()
