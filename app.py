# Main File
# Run this and then ctrl+click on the ip on the console
# Don't forget to shut down the server using ctrl+c in the console


#Importing flask to render the html and collect entered data
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__, static_url_path='/static')


import os # Used for image storage
import sqlite3 # Used for the database

# Setting up the database and creating the cursor
con = sqlite3.connect('database.db')
con = sqlite3.connect('database.db', check_same_thread=False)
pushCur = con.cursor()

# Functionality for the home page
@app.route('/')
def home():
   return render_template('index.html')

# Functionality for the about page
@app.route('/about')
def about():
   return render_template('about.html')


# Path for storing image files
app.config["IMAGE_UPLOADS"] = "C:\\Users\\Alex\\Documents\\GitHub\\TOHacks2022\\images"

# Functionality for the upload images page
@app.route('/upload', methods=["GET", "POST"])
def upload():
   
   if request.method == "POST":

      if request.files:

         # Finding how many users are in the database and creating an extra client number
         clientNum = pushCur.execute('SELECT COUNT(*) FROM clients')
         clientNum = pushCur.fetchone()
         newClientNum = clientNum[0] + 1

         # Retrieving list of text data from text fields in the form
         products = request.form.getlist("input1")

         # Distributing and formating the text data to be used in the database
         fname = products[0]
         fname = "'" + fname + "'"
         print(fname)

         lname = products[1]
         lname = "'" + lname + "'"
         print(lname)

         phoneNum = products[2]
         phoneNum = "'" + phoneNum + "'"
         print(phoneNum)

         symptoms = products[3]
         symptoms = "'" + symptoms + "'"
         print(symptoms)


         # Retrieving uploaded image
         image = request.files["image"]

         # Creating path for image attatched to the database
         # This will be stored in the database
         newClientString = "'" + str(newClientNum) + "'"
         imgPath = "'images\\" + str(newClientNum) + ".png'"


         # Combining given data into a string to be inserted into the database
         strCommand = 'INSERT INTO clients VALUES (' + newClientString + ',' + fname + ',' + lname + ',' + phoneNum + ',' + symptoms + ',' + imgPath + ')'


         #Inserting converted data into database
         pushCur.execute(strCommand)
         con.commit()


         # Renaming and storing image
         image.save(os.path.join(app.config["IMAGE_UPLOADS"], str(newClientNum) + '.png'))
         
         
         return redirect(request.url)

   return render_template('upload.html')


if __name__ == '__main__':
   app.run()