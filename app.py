#Main File
#Run this and then click on the ip on the console


#Importing flask to render the html and collect entered data
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__, static_url_path='/static')

import os
import sqlite3
import shutil


con = sqlite3.connect('database.db')
con = sqlite3.connect('database.db', check_same_thread=False)
pushCur = con.cursor()

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')



app.config["IMAGE_UPLOADS"] = "C:\\Users\\Alex\\Documents\\GitHub\\TOHacks2022\\images"

@app.route('/upload', methods=["GET", "POST"])
def upload():
   
   if request.method == "POST":

      if request.files:

         image = request.files["image"]

         print(image)

         #databasePushRequest.pushToDB("'AAAA'", "'BBBB'", "'416-416-4166'" , "'rash, itchy'" , "'images\\1.png'")

         
         #pushCur = sqlite3.connect('database.db', check_same_thread=False)

         clientNum = pushCur.execute('SELECT COUNT(*) FROM clients')
         clientNum = pushCur.fetchone()
         newClientNum = clientNum[0] + 1
         print("current client is " + str(newClientNum))

         fname = "'AAAA'"
         lname = "'BBBB'"
         phoneNum = "'4164164166'"
         symptoms = "'Rash'"
         imgPath = "'images\\" + str(newClientNum) + ".png'"


         newClientString = "'" + str(newClientNum) + "'"

         #Converting given data into a string to be inserted into the database
         strCommand = 'INSERT INTO clients VALUES (' + newClientString + ',' + fname + ',' + lname + ',' + phoneNum + ',' + symptoms + ',' + imgPath + ')'
         print(strCommand)

         #Inserting converted data into database
         pushCur.execute(strCommand)
         con.commit()

         image.save(os.path.join(app.config["IMAGE_UPLOADS"], str(newClientNum) + '.png'))
         #Renaming and storing image
         #shutil.move(image, 'images/' + str(newClientNum) + '.png')

         return redirect(request.url)

   return render_template('upload.html')


if __name__ == '__main__':
   app.run()