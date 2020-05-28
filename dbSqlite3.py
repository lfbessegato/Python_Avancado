import sqlite3

db = sqlite3.connect('database.db')

c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')

db.commit()
stocks = [('iphone', 100, 2000), ('macbook', 200, 4000)]
print (stocks)
c.executemany('insert into portfolio values(?, ?, ?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)