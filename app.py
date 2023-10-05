# import SQL untuk menggunakan bahasa SQL dalam python
from cs50 import SQL
# import tools utk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

db = SQL("sqlite:///score.db")

@app.route('/', methods=["GET", "POST"]) #root route
def index(): #function index
    if request.method == "POST":
        name = request.form.get("name")
        score = request.form.get("score")
        db.execute("INSERT INTO score (name, score) values(?,?)", name, score)
        return redirect("/")
    else:
        students = db.execute("select * from score")
        return render_template("index.html", students=students)