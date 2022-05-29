#Main File
#Run this and then click on the ip on the console

#Importing flask to render the html and collect entered data
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/upload')
def upload():
   return render_template('upload.html')

if __name__ == '__main__':
   app.run()