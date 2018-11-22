import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = "BACKonLINE.db"
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/getquestion")
def getquestion():
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("SELECT quetsion FROM Questions WHERE questionID = 1")
	data = cur.fetchall()
	print(data)


	return render_template('Template1.html', name = "Humzah", data = data)


# Hard codeed - testing if server is successfully processes data into the DB
''' @app.route("/getquestion")
def testing_data():
	cur.execute("INSERT INTO Clinitions VALUES(4, 5, 'Ryan' )")
	conn.commit()

testing_data()'''




	# try:
		# conn = sqlite.connect(DATABASE)
		# cur = conn.cursor()
		# cur.execute("SELECT quetsion FROM Questions WHERE questionID = 1")
		# data = cur.fetchall()
		# print(data)
	# except:
	#     print("An Error has occured", data)
	#     conn.close()
	# finally:
	#     conn.close()
	#     return str(data)





@app.route("/submitoption")
def submitoption():
	return "Submission has been sent"  # Needs printing?

if __name__ == "__main__":
	app.run(debug=True)

testing_data()
