from flask import Flask, render_template
import sys
import pandas as pd
from contents import __CONTENTS__

# create flask app
app = Flask(__name__)

# use only main menu with bootstrap tables to load contents.
@app.route('/')
def homepage():
    df = pd.read_csv("./static/data/googleplaystore.csv").sample(30)
    return render_template("main.html", data=df, __CONTENTS__=__CONTENTS__)

# login path
@app.route('/login/', methods=["GET","POST"])
def login_page():
    return render_template("login.html") 

# error handling page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", err=str(e))

if __name__ == "__main__":
    app.run()