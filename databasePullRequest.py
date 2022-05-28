# For API intergration
# Allows a user to retrieve information from the database
# Should only be accessable to some users(doctors and stuff)

import sqlite3
import cv2



con = sqlite3.connect('database.db')

pullCur = con.cursor()

# Function for pulling data from the database
# Will pull all of the data and print it row by row
def pullFromDatabase():
    for row in pullCur.execute('SELECT * FROM clients'):
        clientNumber = row[0]
        fname = row[1]
        lname = row[2]
        phoneNum = row[3]
        symptoms =  row[4]
        imgPath = row[5]

        # Temporary code for displaying image that is linked to the database
        # Will be displayed on the website, so this code will not be needed
        img = cv2.imread(imgPath,0)
        cv2.imshow(imgPath,img)
        cv2.waitKey()
        

pullFromDatabase()