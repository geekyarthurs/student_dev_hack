from flask import Flask, render_template, url_for, flash, redirect, session, request
import math
from ai_api import detect_image
app = Flask(__name__, static_folder='static')
app.secret_key = 'prapannaisniceguyhehasfivegirlfriends'
app.config['MONGO_URI'] = "mongodb://localhost:27017/student_dev_hack"



@app.route("/")
def landing_page():
    return render_template("index.html")


@app.route("/detect", methods=["GET", "POST"])
def detect():
    try:

        if request.method == "POST":

            
            
            f = request.files['file']
            f.save(f.filename)
            filename = f.filename
            detectedClasses = detect_image(filename)
            image_classified = detectedClasses["images"][0]["classifiers"][0]["classes"]
            images = [obj["class"] for obj in image_classified]
            # print(images)

            foods = {"bread": {
                "fullname": "Selroti",
                "ingredients": ["rice flour", "water", "sugar", "butter"],
                "types": ["Indian", "Nepali", "Newari"],
                "variations": ["SelRoti Tarkari", "Selroti Chiya", "Selroti Dahi"],
                "price": "Rs. 100",
                "energy": "60 kcal",
                "imageUrl": "https://i.ytimg.com/vi/QvQy2ifqoHU/maxresdefault.jpg"

            }, "flour": {
                "fullname": "Selroti",
                "ingredients": ["rice flour", "water", "sugar", "butter"],
                "types": ["Indian", "Nepali", "Newari"],
                "variations": ["SelRoti Tarkari", "Selroti Chiya", "Selroti Dahi"],
                "price": "Rs. 100",
                "energy": "60 kcal",
                "imageUrl": "https://i.ytimg.com/vi/QvQy2ifqoHU/maxresdefault.jpg"

            }, "wheat flour": {
                "fullname": "Selroti",
                "ingredients": ["rice flour", "water", "sugar", "butter"],
                "types": ["Indian", "Nepali", "Newari"],
                "variations": ["SelRoti Tarkari", "Selroti Chiya", "Selroti Dahi"],
                "price": "Rs. 100",
                "energy": "60 kcal",
                "imageUrl": "https://i.ytimg.com/vi/QvQy2ifqoHU/maxresdefault.jpg"

            }, "wontons": {
                "fullname": "MOMO",
                "ingredients": ["white-flour", "meat", "vegetable", "tomato chutney", "tomato soup", "soyabean"],
                "variations": ["steam-momo", " Kothey momo", "C-momo", "Fry-momo", "Open-momo", "fried momo"],
                "energy": "400 kcal",
                "imageUrl": "https://checkplease.wttw.com/sites/default/files/momo.jpg",
                "price": "Rs. 150"
            }, "dumplings": {
                "fullname": "MOMO",
                "ingredients": ["white-flour", "meat", "vegetable", "tomato chutney", "tomato soup", "soyabean"],
                "variations": ["steam-momo", " Kothey momo", "C-momo", "Fry-momo", "Open-momo", "fried momo"],
                "energy": "400 kcal",
                "imageUrl": "https://checkplease.wttw.com/sites/default/files/momo.jpg",
                "price": "Rs. 150"
            }, "samosa": {
                "fullname": "Samosa",
                "ingredients": ["white-flour", "vegetable", "peas", "peanuts", "soyabean", "potato"],
                "variations": ["indian", "nepali", "chaat"],
                "price": "Rs. 100",
                "energy": "60 kcal",
                "imageUrl": "https://m.recipes.timesofindia.com/recipes/samosa/photo/61050397.cms"
            }}


        for image in images:

            if image in foods.keys():
                return render_template("foods.html", foods=foods[image])
            else:
                return render_template("index.html", error="CANNOT PROCESS!")
    except:
        return render_template("index.html", error="INTERNET ISSUE!")


app.run(debug=True)

