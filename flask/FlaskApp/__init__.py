from flask import Flask, render_template
import sys
import pandas as pd

app = Flask(__name__)

contents = { "index" : [("Home", "/"),("dashboard", "/dashboard")]}

@app.route('/')
def homepage():
    #df = pd.DataFrame({"A": [1,2,3,4,5], "B": [6,7,8,9,10]})
    df = pd.read_csv("./static/data/googleplaystore.csv").sample(30)
    return render_template("main.html", data=df, columns=df.columns, datalen=len(df))

@app.route('/dashboard')
def dashboard():
    df = pd.DataFrame({"A": [1,2,3,4,5], "B": [6,7,8,9,10]})
    return render_template("dashboard.html", data=df, columns=df.columns, datalen=len(df))

if __name__ == "__main__":
    app.run()