import sqlite3
print(sqlite3.version)
conn = sqlite3.connect("test.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute('SELECT * FROM users')
for row in c:
    print(row['name'])
conn.close()







