import sqlite3
print(sqlite3.version)
conn = sqlite3.connect("test.db")
print(conn)
c = conn.cursor()
c.execute("create table if not exists users(id integer primary key, name text, age integer) ")
conn.commit()
conn.close()




