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
	questionID = 1
	cur.execute("SELECT question FROM Questions WHERE questionID = ?", (questionID,))
	question = cur.fetchone()
	cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (questionID,))
	options = cur.fetchall()
	print(question,options)

	resp = make_response(render_template('Template1.html', name = "Humzah", question = question[0], options = options))
	resp.set_cookie('questionID', '1')


	return resp


# Hard codeed - testing if server is successfully processes data into the DB
# @app.route("/getquestion")
# def testing_data():
# 	cur.execute("INSERT INTO Clinitions VALUES(4, 5, 'Ryan' )")
# 	conn.commit()
#
# testing_data()
#



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
	nextquestion = int(request.cookies.get('questionID'))
	print(nextquestion)
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	questionID = nextquestion + 1
	cur.execute("SELECT question FROM Questions WHERE questionID = ?", (questionID,))
	question = cur.fetchone()
	cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (questionID,))
	options = cur.fetchall()
	print(question,options)

	resp = make_response(render_template('Template1.html', name = "Humzah", question = question[0], options = options))
	resp.set_cookie('questionID', '1')


	return resp

	# return "Submission has been sent"  # Needs printing?

if __name__ == "__main__":
	app.run(debug=True)

testing_data()
