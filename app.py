#Main File
#Run this and then click on the ip on the console

import databasePushRequest

#Importing flask to render the html and collect entered data
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/upload', methods=['GET'])
def upload():
   #uploaded_file = request.files['file']
   #if(uploaded_file.filename != ''):
      #uploaded_file.save(uploaded_file.filename)
      #print(uploaded_file.filename)
   #databasePushRequest.pushToDB("'AAAA'", "'BBBB'", "'416-416-4166'" , "'rash, itchy'" , "'images\\1.png'")
   return render_template('upload.html')

if __name__ == '__main__':
   app.run()