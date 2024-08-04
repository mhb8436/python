import sqlite3
print(sqlite3.version)
conn = sqlite3.connect("test.db")
print(conn)
c = conn.cursor()

c.execute('SELECT * FROM users')
for row in c:
    print(row)
conn.close()




