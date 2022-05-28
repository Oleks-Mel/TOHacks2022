#Creates a table in the database, used for debugging


import sqlite3
con = sqlite3.connect('database.db')

cur = con.cursor()

cur.execute('''CREATE TABLE clients
               (clientNumber integer, firstName text, lastName text, phoneNumber text, symptoms text, imagePath text)''')

cur.close()