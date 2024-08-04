import sqlite3
print(sqlite3.version)
conn = sqlite3.connect("test.db")
print(conn)
c = conn.cursor()

c.execute("SELECT * FROM users where name like '%민지%' ")
print(c.fetchone())
conn.close()







