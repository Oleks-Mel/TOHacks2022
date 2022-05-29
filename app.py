#Main File
#Run this and then click on the ip on the console

#Importing flask to render the html and collect entered data
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()