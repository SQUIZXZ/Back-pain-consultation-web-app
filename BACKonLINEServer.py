import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = "BACKonLINE.db"

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/getquestion")
def getquestion():
    return render_template('Template1.html', name = "Humzah")




@app.route("/submitoption")
def submitoption():
    return "Submission has been sent"

if __name__ == "__main__":
    app.run(debug=True)
