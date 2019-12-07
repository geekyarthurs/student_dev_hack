from flask import Flask
import PyMongo
import math
app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def landing_page():

    



app.run()
