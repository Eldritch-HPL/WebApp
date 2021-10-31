# Defines Flask web skeleton with 2 pages

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/Interactive_World_Map/')
def Interactive_World_Map():
    return render_template("Interactive_World_Map.html")

if __name__ == "__main__":
    app.run(debug = False)
    