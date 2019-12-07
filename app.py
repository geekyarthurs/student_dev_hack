from flask import Flask, render_template, url_for, flash, redirect, session, request
import math
from flask_pymongo import PyMongo
app = Flask(__name__)
app.secret_key = 'prapannaisniceguyhehasfivegirlfriends'
app.config['MONGO_URI'] =  "mongodb://localhost:27017/student_dev_hack"
mongo = PyMongo(app)


@app.route("/")
def landing_page():
    users = mongo.db.users.find()
    print(users[0])
    # return "OK" 





@app.route("/login", methods= ["POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = mongo.db.users.find_one({"email": email, "password": password})
        if users:
            session['username'] = users['username']
            session["_id"] = users["_id"]
            return redirect("/dashboard")
        else:
            error = "Invalid Username or Password"
            return "INVALID"



@app.route("/dashboard")
def home():
    id = session["_id"]
    user = mongo.db.users.find_one({"_id": "id"}
    return render_template("dashboard.html")




app.run()
