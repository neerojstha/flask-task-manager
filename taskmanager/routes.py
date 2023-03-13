from flask import render_template
from taskmanager import app, db
from taskmanager.module import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")