import sqlite3
print(sqlite3.version)
conn = sqlite3.connect("test.db")
print(conn)
c = conn.cursor()

c.execute("INSERT INTO users (name, age) VALUES ('민지', 19)")
c.execute("INSERT INTO users (name, age) VALUES ('하니', 21)")
c.execute("INSERT INTO users (name, age) VALUES ('혜린', 19)")
c.execute("INSERT INTO users (name, age) VALUES ('수지', 20)")

conn.commit()
conn.close()






