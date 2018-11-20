import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = "BACKonLINE.db"

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
	return "Submission has been sent"

if __name__ == "__main__":
	app.run(debug=True)
