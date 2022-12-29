from portfolio import app

# import render template
from flask import render_template, url_for

@app.get("/")
def index():
    return render_template("index.html")


