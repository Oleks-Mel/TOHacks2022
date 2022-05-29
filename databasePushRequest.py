# For API intergration
# Allows a user to push information to the database
# Should only be accessable to some users(doctors and stuff)

import os
import sqlite3


con = sqlite3.connect('database.db')
pushCur = con.cursor()


#Function that pushes data to the database to be stored and retrieved when needed
def pushToDB(fname, lname, phoneNum , symptoms, imgPath):



    #Checks number of clients currently in the database and adds another client number for the client
    clientNum = pushCur.execute('SELECT COUNT(*) FROM clients')
    clientNum = pushCur.fetchone() 
    newClientNum = clientNum[0] + 1
    print("current client is " + str(newClientNum))


    newClientString = "'" + str(newClientNum) + "'"

    #Converting given data into a string to be inserted into the database
    strCommand = 'INSERT INTO clients VALUES (' + newClientString + ',' + fname + ',' + lname + ',' + phoneNum + ',' + symptoms + ',' + imgPath + ')'
    print(strCommand)

    #Inserting converted data into database
    pushCur.execute(strCommand)
    con.commit()

    #Renaming file, 
    #os.rename('images\\14 copy.png', "images\\" + str(newClientNum) + '.png')

# For testing, remove in fanal version
pushToDB("'First Name'", "'Last Name'", "'416-416-4166'" , "'rash, itchy'" , "'images\\1.png'")