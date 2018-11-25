import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = "BACKonLINE.db"
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
questionID = 1
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/getquestion", methods =["GET", "POST"])
def getquestion():
	global questionID
	options_list, question, questionNum, template = return_question()



	# resp.set_cookie('questionID', '1')
	if request.method == "POST":
		if request.form["submit_button"] == "Next":
			hey = request.args.get("question-options")
			print(hey)
			test1 = request.form["option"]
			print("TES",test1)
			hey1 = request.args.get("option")
			print("es",hey1)
			question_result = request.form.getlist("option")
			for result in question_result:
				print(f"{result} has a value of {return_from_db(result)[0]}")
			questionID = questionID + 1
			options_list, question, questionNum, template = return_question()
			print("increment")
			#resp.set_cookie('questionID', str(questionID))
			#return resp
		elif request.form["submit_button"] == "Back":
			print("back pressed")
			questionID = questionID - 1
			options_list, question, questionNum, template = return_question()
			print("decrement")
			#resp.set_cookie('questionID', str(questionID))
			#return resp
	resp = make_response(render_template(template, name = "Humzah", question = question[0], options = options_list, questionNum = questionNum))
	return resp
def return_question():
	global questionID
	#questionID = int(request.cookies.get('questionID'))
	print("testQ",questionID)

	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()

	cur.execute("SELECT questionID FROM Questions WHERE questionID = ?", (questionID,))
	questionNum = cur.fetchone()
	cur.execute("SELECT question FROM Questions WHERE questionID = ?", (questionID,))
	question = cur.fetchone()
	cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (questionID,))
	options = cur.fetchall()
	print(question,options,questionNum)
	cur.execute("SELECT questionType FROM Questions WHERE questionID =?",(questionID,))
	# type = cur.fetchone()
	cur.execute("SELECT questionType FROM QuestionTypes WHERE typeID =?",(cur.fetchone()))
	question_type = cur.fetchone()[0]
	if question_type == "Multiple-Answer":
		print("MULT")
		template = "Multiple-Answer.html"
	elif question_type == "Single-Answer":
		print("SINGLE")
		template = "Single-Answer.html"
	elif question_type == "Slider":
		print("Slider")
		template = "Slider.html"
	elif question_type == "Text-Field":
		print("TEXT FIELD")
		template = "Text-Field.html"
	else:
		print("There is something wrong",question_type)

	options_list = []

	for option in options:
		options_list.append(option[0])
	return options_list, question, questionNum, template

def return_from_db(item):
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("SELECT questionValue FROM Options Where optionText = ?",(item,))
	# print(cur.fetchone())
	return cur.fetchone()

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
	cur.execute("SELECT questionID FROM Questions WHERE questionID = ?", (questionID,))
	questionNum = cur.fetchone()
	cur.execute("SELECT question FROM Questions WHERE questionID = ?", (questionID,))
	question = cur.fetchone()
	cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (questionID,))
	options = cur.fetchall()
	print(questionNum,question,options)

	resp = make_response(render_template('Template1.html', name = "Humzah", question = question[0], options = options, questionNum = questionNum))
	resp.set_cookie('questionID', '1')


	return resp

	# return "Submission has been sent"  # Needs printing?

if __name__ == "__main__":
	app.run(debug=True)

testing_data()
