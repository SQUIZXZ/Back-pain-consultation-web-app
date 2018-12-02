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
		if request.form["submit_button"] == "Next >":
			hey = request.args.get("question-options")
			#print(hey)
			test1 = request.form["option"]
			#print("TES",test1)
			hey1 = request.args.get("option")
			#print("es",hey1)
			question_result = request.form.getlist("option")

			for result in question_result:
				if result == "":
					pass
				else:
					print(f"{result} has a value of {return_from_db(result)[0]}")
				#print(f"{result} has a value of {return_from_db(result)[0]}")
			writethings( question_result,questionNum)
			questionID = questionID + 1
			options_list, question, questionNum, template = return_question()
			#print("increment")

			#resp.set_cookie('questionID', str(questionID))
			#return resp
		elif request.form["submit_button"] == "< Back":
			#print("back pressed")
			questionID = questionID - 1
			options_list, question, questionNum, template = return_question()
			#print("decrement")
			#resp.set_cookie('questionID', str(questionID))
			#return resp
	resp = make_response(render_template(template, name = "Humzah", question = question[0], options = options_list, questionNum = questionNum))
	return resp
def writethings(question_result,question_number):
	print("Values passed", question_result, question_number)
	print("Working")
	values = []
	for result in question_result:

		print("Inside",result)
		value = return_from_db(result)[0]
		print("restunred value",value)
		values.append(value)
		try:
			conn.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("SELECT optionID FROM Options WHERE optionText = ?", (result,))
			fetched = cur.fetchone()
			print("Fetched ID for ***", result)
		except:
			pass
	print("values list",values)

	#result_value = return_from_db(q_result)[0]
	#need to get the quetsionID and the optionID for each question added
	try:
		print('into the try')
		conn = sqlite3.connect(DATABASE)
		print('into the try111')
		cur = conn.cursor()
		print('into the try222')
		cur.execute("INSERT INTO Results ('patientID', 'questionID', 'optionID', 'optionValue') VALUES (?,?,?,?)",(1,question_number[0],2,values))
		print('into the try333')
		conn.commit()
		conn.close()
		print('into the try444')
		msg = "record saved successfully"
	except:
		#conn.rollback()
		print('rollback')
		msg = "An error has occured"
	finally:

		print('finllay')
		return msg
	# print("Writing data into database")
	# #print('tititititi')
	# # if request.method == "POST":
	# # 	option = request.form.get('option', default="Error")
	# # 	print("Inserting"+option)
	# try:
	# 	#print('into the try')
	# 	conn = sqlite3.connect(DATABASE)
	# 	#print('into the try111')
	# 	cur = conn.cursor()
	# 	#print('into the try222')
	# 	cur.execute("INSERT INTO Results ('patientID', 'questionID', 'optionID', 'optionValue') VALUES (?,?,?,?)",(1,1,2,0))
	# 	#print('into the try333')
	# 	conn.commit()
	# 	#print('into the try444')
	# 	msg = "record saved successfully"
	# except:
	# 	conn.rollback()
	# 	#print('rollback')
	# 	msg = "An error has occured"
	# finally:
	# 	conn.close()
	# 	#print('finllay')
	# 	return msg






def return_question():
	global questionID
	#questionID = int(request.cookies.get('questionID'))
	#print("testQ",questionID)

	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()

	cur.execute("SELECT questionID FROM Questions WHERE questionID = ?", (questionID,))
	questionNum = cur.fetchone()
	cur.execute("SELECT question FROM Questions WHERE questionID = ?", (questionID,))
	question = cur.fetchone()
	cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (questionID,))
	options = cur.fetchall()
	#print(question,options,questionNum)
	cur.execute("SELECT questionType FROM Questions WHERE questionID =?",(questionID,))
	# type = cur.fetchone()
	cur.execute("SELECT questionType FROM QuestionTypes WHERE typeID =?",(cur.fetchone()))
	question_type = cur.fetchone()[0]
	cur.close()
	if question_type == "Multiple-Answer":
		#print("MULT")
		template = "Multiple-Answer.html"
	elif question_type == "Single-Answer":
		#print("SINGLE")
		template = "Single-Answer.html"
	elif question_type == "Slider":
		#print("Slider")
		template = "Slider.html"
	elif question_type == "Text-Field":
		#print("TEXT FIELD")
		template = "Text-Field.html"
	else:
		print("There is something wrong",question_type)
	options_list = []
	for option in options:
		options_list.append(option[0])
	return options_list, question, questionNum, template

def return_from_db(item):
	#print("Returning values",item)
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("SELECT questionValue FROM Options Where optionText = ?",(item,))
	fetched = cur.fetchone()
	#print("fetched",fetched)
	if fetched == None: #if the question has a text field, then will return a NoneType
		fetched = (0,)
	# print(cur.fetchone())
	cur.close()
	return fetched

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

# testing_data()
