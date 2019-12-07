from flask import Flask, render_template, url_for, flash, redirect, session
import math
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_URI'] =  "mongodb://localhost:27017/student_dev_hack"
mongo = PyMongo(app)


@app.route("/")
def landing_page():
    users = mongo.db.users.find()
    print(users[0])
    # return "OK" 





@app.route("/login")
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = mongo.db.users.find_one({"email": email, "password": password})
        if users:
            session['username'] = username


@app.route("/register"):


if __name__ == '__main__':  
   app.run(debug = True)  