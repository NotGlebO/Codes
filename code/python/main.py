import sqlite3

db=sqlite3.connect('client.db')

c = db.cursor()

c.execute("INSERT INTO data (user, password, id) VALUES ('Gleb', 'qwerty', 2567)")
db.commit()
db.close()