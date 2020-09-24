import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()


for row in cursor.execute('SELECT * FROM contracts'):
    print(row)
