import sqlite3
import Time

check = 0
method = '0'
conn = sqlite3.connect("app.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS history(
            num INTEGER,
            partId TEXT,
            owner TEXT,
            time TEXT,
            date TEXT
            )""")


def hist():
    name = input("Enter Name: ")
    print(name)
    item = input("Item: ")
    c.execute("SELECT * FROM history")
    num = (c.fetchall())
    order = (len(num) + 1)
    c.execute("INSERT INTO history VALUES (?,?,?,?,?)", (order, item, name, Time.time(), Time.date()))
    conn.commit()


hist()

c.execute("SELECT * FROM history")
list1 = (c.fetchall())

for x in reversed(range(len(list1))):
    # print(x)
    print(list1[x])

# print(list1)

conn.commit()
conn.close()
