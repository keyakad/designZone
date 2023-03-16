from flask import Flask, render_template, request
from functions import colorPalette, imageSearcher
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        if "submit1" in request.form:
            query = request.form["image"]
            num = request.form["num"]
            access_key = request.form["key"]
            img = imageSearcher(query, num,access_key)
            return render_template('results.html', img=img, num = int(num))

@app.route("/colorp", methods=["GET", "POST"])
def colorp():
    if "submit5" in request.form:
        user_color = request.form["color-toggle"][1:]
        red = int(user_color[:2], 16)
        green = int(user_color[2:4], 16)
        blue = int(user_color[4:], 16)
        result = colorPalette(red, green, blue)
        return render_template('colorp.html', results=result)

@app.route("/selectpage", methods=["GET", "POST"])
def selectpage():
    if request.method == "POST":
        if "submit4" in request.form:
            if "card" in request.form:
                moodboard_card = request.form.getlist("card")
            return render_template('selectpage.html', moodboard_card = moodboard_card)
