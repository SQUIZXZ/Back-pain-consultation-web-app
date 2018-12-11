import os
from flask import Flask, redirect, request, render_template, make_response, escape, session, url_for, flash
import sqlite3
from datetime import datetime
import time
from functools import wraps

DATABASE = "BACKonLINE.db"
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
# questionID = 1
app = Flask(__name__)
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/", methods = ["GET","POST"])
def show_home():
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	return redirect("Login")
# @app.route("/login", methods = ["GET","POST"])
# def login():
# 	if request.method == "POST":
# 		print("acualy working")
# 		email = request.form["email"]
# 		password = request.form["password"]


@app.route("/getquestion/<int:patient_id>/<int:form_id>/<int:question_number>", methods =["GET", "POST"])

def getquestion(form_id,patient_id,question_number):
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	elif session.get('usertype') != 'Patient':
		return "ERROR - Permission required"

	# global questionID
	print("CURRENT QUETSOPN", question_number)
	options_list, question, questionNum, template, option_texts, fetched_texts = return_question(question_number,patient_id,form_id)
	print("FETHCED ££££", option_texts, fetched_texts)
	attemptNumber = 1


	# resp.set_cookie('questionID', '1')
	if request.method == "POST":
		if "Next" in request.form:
			# hey = request.args.get("question-options")
			# #print(hey)
			# test1 = request.form["option"]
			# #print("TES",test1)
			# hey1 = request.args.get("option")
			#print("es",hey1)
			question_result = request.form.getlist("option")

			# for result in question_result:
			# 	if result == "":
			# 		pass
			# 	else:
			# 		print(f"{result} has a value of {return_from_db(result,questionID)[0]}")
			# 	#print(f"{result} has a value of {return_from_db(result)[0]}")

			writethings(patient_id, question_result,questionNum,attemptNumber, form_id)
			# questionID = questionID + 1
			question_number += 1
			if question_number > 39:
				question_number = 39
				return redirect("submit_assessment/"+str(patient_id)+"/"+str(form_id))
			# options_list, question, questionNum, template = return_question(question_number,patient_id,form_id)
			#print("increment")
			return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(question_number))

			#resp.set_cookie('questionID', str(questionID))
			#return resp
		elif "Back" in request.form:
			#print("back pressed")
			# questionID = questionID - 1
			question_number -= 1
			if question_number == 0:
				question_number = 1
			# options_list, question, questionNum, template = return_question(question_number,patient_id,form_id)
			#print("decrement")
			#resp.set_cookie('questionID', str(questionID))
			#return resp
			return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(question_number))
	resp = make_response(render_template(template, name = "Humzah", question = question[0], options = options_list, questionNum = questionNum, id = patient_id, selected_options = option_texts, selected_texts =fetched_texts  ))
	return resp
def writethings(patient_id,question_result,question_number,attemptNumber, form_id):
	print("Values passed", question_result, question_number)
	print("Working")
	values = []
	option_ids = []
	for result in question_result:

		print("Inside",result, str(result))
		value_of_result, id_of_result = return_from_db(result,question_number)
		print("restunred value",value_of_result)
		print("ID RETURNED", id_of_result)
		values.append(value_of_result[0])
		option_ids.append(id_of_result[0])
		print("TRYING..")
		# conn = sqlite3.connect(DATABASE)
		# cur = conn.cursor()
		# print("TRYING....")
# 		try:
# #### Need to change the select so it selects the optino fromt he correct question
#
# 			# cur.execute("SELECT optionID FROM Options INNER JOIN Questions ON Options.questionID = ? and Questions.questionID = ? AND Options.optionText = ?",(question_number,question_number,result,))
# 			cur.execute("SELECT optionID FROM Options WHERE optionText = ? AND questionID = ?", (str(result),question_number[0],))
# 			fetched = cur.fetchone()
# 			if fetched == None:
# 				cur.execute("SELECT optionID FROM Options WHERE questionID = ?", (question_number[0],))
# 				fetched = cur.fetchone()
#
# 			print("Fetched ID for ***", result, fetched)
# 		except:
# 			print("SOMETHING WENT WRONG")
	if len(values) == 1:
		values = values[0]
	else:
		str_values = [str(value) for value in values]
		values = ",".join(str_values)
	if len(option_ids) == 1:
		option_ids = option_ids[0]
	else:
		str_ids = [str(id) for id in option_ids]
		option_ids = ",".join(str_ids)

	print("values list",values)
	print("ids list", option_ids)
	text = ""
	#result_value = return_from_db(q_result)[0]
	#need to get the quetsionID and the optionID for each question added
	try:
		print('into the try')
		conn = sqlite3.connect(DATABASE)
		print('into the try111')
		cur = conn.cursor()
		print('into the try222')

		if question_number[0] == 3:
			text = question_result[0]
			print("NEW TEXT",text)
		print(f"before insert Q:{question_number[0]} Option ID: {option_ids} Text: {text} Option Values:{values} FORM: {form_id} ")
		returned_bool = check_if_form_question_exists(form_id,question_number[0])
		print("RETURNED BOOL",returned_bool)
		if returned_bool == True:
			print("We will need to update")
			print(option_ids,text,values,form_id,question_number[0],patient_id)
			try:

				cur.execute("UPDATE Results SET optionID = ? , textField = ?, optionValue = ? WHERE form_id =? AND questionID = ? AND patientID = ? ",(option_ids,text,values,form_id,question_number[0],patient_id,))
				conn.commit()
				print("Worked")
			except:
				print("Not working")
			msg = "IPDATE NEEDED"
		else:
			print("We will need to insert a new row")
			cur.execute("INSERT INTO Results ('patientID', 'questionID', 'optionID', 'optionValue', 'textField','form_id') VALUES (?,?,?,?,?,?)",(patient_id,question_number[0],option_ids,values,text,form_id,))
			print('into the try333')
			conn.commit()

			print('into the try444')
			msg = "record saved successfully"
	except:
		#conn.rollback()
		print('rollback')
		msg = "An error has occured"
	finally:
		conn.close()

		print('finllay')
		print(msg)
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




def check_if_form_question_exists(form_id,question_number):
	try:
		print("INTO TRY OF DEF",form_id, question_number)
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		cur.execute("SELECT EXISTS(SELECT 1 FROM Results WHERE (form_id = ? AND questionID=? ))",(form_id,question_number))
		fetched_boolean = cur.fetchone()[0]
		print("Boolean:",bool(fetched_boolean))
	except:
		conn.rollback()
		print('ROOUJLKKJ')
	finally:

		conn.close()
	return bool(fetched_boolean)

# def return_question(question_number):
# 	# global questionID
# 	#questionID = int(request.cookies.get('questionID'))
# 	#print("testQ",questionID)
#
# 	conn = sqlite3.connect(DATABASE)
# 	cur = conn.cursor()
#
# 	cur.execute("SELECT questionID FROM Questions WHERE questionID = ?", (question_number,))
# 	questionNum = cur.fetchone()
# 	cur.execute("SELECT question FROM Questions WHERE questionID = ?", (question_number,))
# 	question = cur.fetchone()
# 	cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (question_number,))
# 	options = cur.fetchall()
#
# 	#used to get the template which will
# 	#print(question,options,questionNum)
# 	cur.execute("SELECT questionType FROM Questions WHERE questionID =?",(question_number,))
# 	type = cur.fetchone()[0]
# 	print("TYPEID",type)
# 	cur.execute("SELECT questionType FROM QuestionTypes WHERE typeID =?",(type))
# 	question_type = cur.fetchone()[0]
# 	cur.close()
# 	if question_type == "Multiple-Answer":
# 		#print("MULT")
# 		template = "Multiple-Answer.html"
# 	elif question_type == "Single-Answer":
# 		#print("SINGLE")
# 		template = "Single-Answer.html"
# 	elif question_type == "Slider":
# 		#print("Slider")
# 		template = "Slider.html"
# 	elif question_type == "Text-Field":
# 		#print("TEXT FIELD")
# 		template = "Text-Field.html"
# 	else:
# 		print("There is something wrong",question_type)
# 	options_list = []
# 	for option in options:
# 		options_list.append(option[0])
# 	print("LIST OF OPTIONS FOR QUESTION",options_list)
# 	return options_list, question, questionNum, template
def return_question(question_number,patient_id,form_id):
	# global questionID
	#questionID = int(request.cookies.get('questionID'))
	#print("testQ",questionID)
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()

		cur.execute("SELECT questionID FROM Questions WHERE questionID = ?", (question_number,))
		questionNum = cur.fetchone()
		cur.execute("SELECT question FROM Questions WHERE questionID = ?", (question_number,))
		question = cur.fetchone()
		cur.execute("SELECT optionText FROM Options WHERE questionID = ?", (question_number,))
		options = cur.fetchall()

		#used to get the template which will
		#print(question,options,questionNum)
		cur.execute("SELECT questionType FROM Questions WHERE questionID =?",(question_number,))
		type = cur.fetchone()[0]
		print("TYPEID",type)
		cur.execute("SELECT questionType FROM QuestionTypes WHERE typeID =?",(type))
		question_type = cur.fetchone()[0]
	except:
		conn.rollback()
		print("rolling back")
	finally:
		cur.close()

	returned_bool = check_if_form_question_exists(form_id,question_number)
	print("RETURNED BOOL FOR PERSISTENCY",returned_bool)
	if returned_bool == True:
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			print("The row exists in the results", question_number)
			cur.execute("SELECT optionID, textField FROM Results WHERE form_id = ? AND questionid = ?;",(form_id,question_number,))
			fetched_options_texts = cur.fetchall()
			print("LISTED FETECHELJK",fetched_options_texts )
			print(list(fetched_options_texts[0]))
			listed_fetch = list(fetched_options_texts[0])
			fetched_options = listed_fetch[0]
			fetched_texts = listed_fetch[1].split(",")

			print("%%%%%%%%%%%%%%%%%%%%%%",fetched_options)


			fetched_options = fetched_options.split(",")
			option_texts =[]
			for item in fetched_options:
				print(item)
				try:
					cur.execute("SELECT optionText FROM Options WHERE optionID = ?",(int(item),))
					option_texts.append(cur.fetchone()[0])

				except:
					conn.rollback()
					print("ROLLING FROM inside question")
				finally:
					pass


			print("££££££££££££", fetched_texts)





			# for item in listed_fetch:
			# 	if item == "":
			# 		print("empty")
			# 		pass
			# 	elif item.split(",") > 1:
			# 		split_options = item.split(",")
			# 		print(split_options)



			print("LISTED ggrgr")

		except:
			conn.rollback()
			print("ROLLING FROM return question")
		finally:
			cur.close()
		print(option_texts, fetched_texts)
		fetched_texts = ':'.join(fetched_texts)
		option_texts = ':'.join(option_texts)
		print("£$%£$%^&%&&^%&%", fetched_texts, option_texts)


	else:
		print("The row doens't exist in the results",question_number)
		option_texts =[]
		fetched_texts = []





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
	print("LIST OF OPTIONS FOR QUESTION",options_list)
	return options_list, question, questionNum, template, option_texts, fetched_texts

def return_from_db(item, question_number):
	print("Returning values",item, question_number)
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("SELECT questionValue FROM Options Where optionText = ?",(item,))
	fetched_value = cur.fetchone()
	#print("fetched",fetched)
	if fetched_value == None: #if the question has a text field, then will return a NoneType
		fetched_value = (0,)
	cur.execute("SELECT optionID FROM Options WHERE optionText = ? AND questionID = ?", (str(item),question_number[0],))
	fetched_id = cur.fetchone()
	if fetched_id == None:
		cur.execute("SELECT optionID FROM Options WHERE questionID = ?", (question_number[0],))
		fetched_id = cur.fetchone()
	print("Fetched Value ******", fetched_value)
	print("Fetched ID for ***", item, fetched_id)
	# print(cur.fetchone())
	cur.close()
	return fetched_value, fetched_id


@app.route("/submit_assessment/<int:patient_id>/<int:form_id>", methods = ["GET","POST"])
def submit(patient_id,form_id):
	if request.method == "GET":
		print("SUBMITTING", patient_id, form_id)
		return render_template("Submit.html", patient_id = patient_id, form_id =form_id )
	if request.method == "POST":
		print("POSTING")
		if "Submit" in request.form:
			i = datetime.now()
			current_date = i.strftime("%d-%m-%Y")
			stringed_date = current_date.split("-")
			print(stringed_date)
			current_time = i.strftime("%H:%M:%S:%f")
			stringed_time = current_time.split(":")
			print(stringed_time)
			stringed_date_time = current_date + "," + current_time
			print(stringed_date_time)
			try:
				conn = sqlite3.connect(DATABASE)
				cur = conn.cursor()
				print("1")
				scores = calculate_scores(form_id)

				# cur.execute("UPDATE FormSubmissions SET completed = ? , dateSubmitted = ? WHERE id = ?",("True",stringed_date_time,int(form_id),))
				cur.execute("UPDATE FormSubmissions SET completed = ? , dateSubmitted = ?, totalScores = ? WHERE id = ?",("True",stringed_date_time,scores,form_id,))
				print("2")
				conn.commit()
				print("3")
			except:
				conn.rollback()
				print("ROLLING FROM return question")
			finally:
				cur.close()

			print("WIll submit")
			try:
				conn = sqlite3.connect(DATABASE)
				print("connected")
				cur = conn.cursor()
				print("cursor")
				cur.execute("SELECT patientName FROM Patients WHERE patientID=?",(int(patient_id),))
				print("executed")
				info = cur.fetchone()
				print(info)
				conn.commit()
				msg = "Retrieved"
			except:
				conn.rollback()
				print("rollbacksdw")
				msg = "error"
			finally:
				conn.close()
			return render_template("Submit-Complete.html", date = current_date, name = info[0], form_id =form_id, id = patient_id  )
		if "Back" in request.form:
			print("WIll go back")
			return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(39))
def calculate_scores(form_id):
	try:
		total_score = 0
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		cur.execute("SELECT SUM(Questions.maxScores) FROM Questions INNER JOIN Results ON Results.questionID = Questions.questionID WHERE Results.form_id = ?",(int(form_id),))
		max_score = cur.fetchone()[0]
		cur.execute("SELECT optionValue FROM Results WHERE form_id = ?;",(int(form_id),))
		patient_scores = cur.fetchall()
		patient_scores = map(list, patient_scores)
		for score in patient_scores:
			if len(score[0]) == 1:
				total_score += int(score[0])
			else:
				scores = score[0].split(",")
				for i in scores:
					total_score += int(i)

			# score = score.split(",")





	except:
		conn.rollback()
		print("rollback")
		msg = "error"
	finally:
		conn.close()
	returning_value = str(total_score) +"/" +str(max_score)
	print("WOAH",returning_value)
	return returning_value
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
@app.route("/SignUp", methods = ['GET'])
def signup():
	if request.method == 'GET':
		return render_template('Signup.html')
@app.route("/Patient/AddPatient", methods = ['POST'])
def patientAddDetails():
	if request.method == 'POST':
		print("IN")
		print(request.form)
		patientName = request.form.get('patientName', default="Error")
		Password = request.form.get('Password', default="Error")
		Email = request.form.get('Email', default="Error")
		Gender = request.form.get('Gender', default="Error")
		Age = request.form.get('Age', default="Error")

		print(patientName,Password, Email, Gender, Age)
		print("Inserting patient"+patientName)
		msg = "FAILURE"
		try:
			conn = sqlite3.connect(DATABASE)
			print("patient1")
			cur = conn.cursor()
			print("patient2")
			cur.execute("SELECT EXISTS(SELECT 1 FROM Patients WHERE (patientName = ? AND Email=?))",(patientName,Email,))
			exists = cur.fetchone()[0]
			if exists == 0:
				# print("inTO THIS")
				cur.execute("INSERT INTO Patients ('patientName', 'Password', 'Email', 'Gender', 'Age') VALUES (?,?,?,?,?)", (patientName, Password, Email,Gender,Age))
				conn.commit()
				msg = "SUCCESS"
			else:
				msg = "EXISTS"
			print("patient3")

		except Exception as e:
			print(e)
			conn.rollback()
			print("SOMETHING WENT WRONG")
			return "Something went wrong, please try again"			# msg = "Error adding patient"
		finally:
			conn.close()
		print(msg)
		return msg

@app.route("/Login", methods = ['GET', 'POST'])
def login():

	if request.method=='POST':
		email = request.form.get('email', default = "Error")
		password = request.form.get('password', default = "Error")
		print(email,password)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			print("BEFORE")
			cur.execute("SELECT EXISTS(SELECT 1 FROM Patients WHERE (Email = ? AND Password=?))",(email,password,))
			print("AFTER")
			patient_exists = cur.fetchone()
			session['logged_in'] = True
			session['email'] = request.form['email']

			print("BEFORE")
			cur.execute("SELECT EXISTS(SELECT 1 FROM Clinitions WHERE (Email = ? AND Password=?))",(email,password,))
			print("AFTER")
			clinition_exists = cur.fetchone()
			print("FETCHED")

			session['logged_in'] = True
			session['email'] = request.form['email']
			# cur.execute("SELECT EXISTS(SELECT 1 FROM Patients WHERE (patientName =? AND Email=?))",(email,password,))
		except:
			print("SOMETHING WENT WRONG")
			conn.rollback()

		if patient_exists[0] == 1:
			cur.execute("SELECT patientID FROM Patients WHERE (Email = ? AND Password=?)",(email,password,))
			id = cur.fetchone()[0]
			session['email'] = request.form['email']
			session['logged_in'] = True
			session['usertype'] = 'Patient'
			print(session)

			return redirect("Home/Patient/"+str(id))
		elif clinition_exists[0] == 1:
			session['email'] = request.form['email']
			session['logged_in'] = True
			session['usertype'] = 'Admin'

			print(session)



			return redirect("Home/Clinition")
		else:

			flash('The email/password combination is invalid')

	return render_template('Login.html')

@app.route('/logout')
def logout():
   session.pop('usertype', None)
   session.pop('email', None)
   print(session)

   flash("You were logged out")
   return redirect(url_for('login'))

def checkCredentials(uName, pw):
	return pw == 'BACKonLINE'

app.secret_key = ' abc123def456ghi789'
##### patient route
@app.route("/Home/Patient/<int:id>", methods = ["GET"])
def p_home(id):
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	elif session.get('usertype') != 'Patient':
		return "ERROR - Permission required"
	delete_any_old_assessments(id)
	try:
		conn = sqlite3.connect(DATABASE)
		print("connected")
		cur = conn.cursor()
		print("cursor")
		cur.execute("SELECT patientName,Email,Age,Gender FROM Patients WHERE patientID=?",(id,))
		print("executed")
		info = cur.fetchone()
		print(info)
		conn.commit()
		msg = "Retrieved"
	except:
		conn.rollback()
		print("rollback")
		msg = "error"
	finally:
		conn.close()

	return render_template("Patient.html", id = id, Email = info[1], Age = info[2], Gender = info[3], Name = info[0])
def delete_any_old_assessments(id):
	try:
		conn = sqlite3.connect(DATABASE)
		print("connected")
		cur = conn.cursor()
		print("cursor")
		cur.execute("SELECT id, dateCreated FROM FormSubmissions WHERE patientID = ?;",(int(id),))
		print("selected")
		fetched_forms = cur.fetchall()
		print("fetched",fetched_forms)


	# past_date = datetime(int(stringed_date[2]),int(stringed_date[1]),int(stringed_date[0]),int(stringed_time[0]),int(stringed_time[1]),int(stringed_time[2]),int(stringed_time[3]))
	#
	# difference = datetime.utcnow() - past_date
	# if (difference.days == 0):
	# 	msg = "Date is within 24 hours"
	#
	# else:
	# 	msg = "You can no longer edit this submisssion"
	except:
		conn.rollback()
		print("rollback")
	finally:
		conn.close()
	fetched_forms = map(list, fetched_forms)
	for form in fetched_forms:
		form_id = form[0]
		print("ID",int(form_id))
		print(form)
		stringed_date_time = form[1].split(",")
		stringed_date = stringed_date_time[0].split("-")
		stringed_time = stringed_date_time[1].split(":")
		past_date = datetime(int(stringed_date[2]),int(stringed_date[1]),int(stringed_date[0]),int(stringed_time[0]),int(stringed_time[1]),int(stringed_time[2]),int(stringed_time[3]))
		print(stringed_date,stringed_time)

		print(past_date)
		difference = datetime.utcnow() - past_date
		print(difference)
		if (difference.days == 0):
			msg = "Date is within 24 hours"

		else:
			msg = "You can no longer edit this submisssion"
			delete_form_from_db(form_id)
		print(msg)
def delete_form_from_db(id):
	print("ID PASSED",id)
	try:
		conn = sqlite3.connect(DATABASE)
		print("connected")
		cur = conn.cursor()
		print("delted")
		cur.execute("DELETE FROM Results WHERE form_id = ?",(id,))
		cur.execute("DELETE FROM FormSubmissions WHERE id = ?",(id,))
		conn.commit()
		print("delete complete")
	except:
		conn.rollback()
		print("rollback")
	finally:
		conn.close()


@app.route("/Home/Patient/<int:user_id>/Edit_Submissions")
def edit_submissions(user_id):
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		print("HEY")
		print(user_id)
		# Gets the date/time time the form was submitted with the id for the specific patient
		cur.execute("SELECT FormSubmissions.dateCreated, FormSubmissions.id FROM FormSubmissions WHERE patientID = ?",(user_id,))
		date_time = cur.fetchone()
		# Gets all of the results for that one submisson (put in differnt app route)
		cur.execute("""SELECT QuestionTypes.questionType,Questions.questionType, Results.questionID, Results.optionID, Results.optionValue, Results.textField, FormSubmissions.dateCreated
		FROM Results INNER JOIN FormSubmissions ON Results.patientID = FormSubmissions.patientID
		INNER JOIN Questions ON Questions.questionID = Results.questionID
		INNER JOIN QuestionTypes ON QuestionTypes.typeID = Questions.questionType
		WHERE FormSubmissions.completed = "False" AND Results.patientID = ?;""",(user_id,))
		# Gets the date created and completed forms from a specific patient
		cur.execute("SELECT dateCreated, id FROM FormSubmissions WHERE patientID = ? AND completed = 'False'", (user_id,))
		submissions_by_patient = cur.fetchall()
		print(submissions_by_patient)
		print(f"Date is {date_time[0]} and time was {date_time[1]}")
	except:
		conn.rollback()
		print("rollback 123456346")
		submissions_by_patient = []


	return render_template("Edit_Submissions.html", submissions = submissions_by_patient, user_id = user_id)
@app.route("/edit_submission/<int:patient_id>/<int:form_id>")
def edit_form(patient_id,form_id):
	print("pateinte",patient_id, "form",form_id)
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		print("1")
		cur.execute("SELECT questionID FROM Results WHERE form_id =? AND patientID =? ORDER BY questionID DESC LIMIT 1",(int(form_id),int(patient_id),))
		print("2")
		fetched_question_number = cur.fetchone()
		print("3", fetched_question_number)
		print("Q NUMER", fetched_question_number[0])
		fetched_question_number = fetched_question_number[0]
	except:
		conn.rollback()
		print("rollback 123456346")
	finally:
		conn.close()
	if fetched_question_number == None:
		fetched_question_number = 1
	return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(fetched_question_number))

@app.route("/New-Assessment/<int:patient_id>")
def new_surver(patient_id):
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	print("USER_ID", patient_id)
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()

	i = datetime.now()
	current_date = i.strftime("%d-%m-%Y")
	stringed_date = current_date.split("-")

	current_time = i.strftime("%H:%M:%S:%f")
	stringed_time = current_time.split(":")

	stringed_date_time = current_date + "," + current_time
	cur.execute("INSERT INTO FormSubmissions (patientID, completed, dateCreated,dateSubmitted,totalScores) VALUES (?,?,?,?,?)",(patient_id,'False',stringed_date_time," "," ",))
	print("DATE-TIME", current_date + "," + current_time,stringed_date_time)
	form_id = cur.lastrowid
	conn.commit()
	conn.close()
	print("FORM ID", form_id)
	past_date = datetime(int(stringed_date[2]),int(stringed_date[1]),int(stringed_date[0]),int(stringed_time[0]),int(stringed_time[1]),int(stringed_time[2]),int(stringed_time[3]))

	difference = datetime.utcnow() - past_date
	if (difference.days == 0):
		msg = "Date is within 24 hours"

	else:
		msg = "You can no longer edit this submisssion"
	print("TIME DIFFERENCE", difference)
	print(i,past_date)
	print(msg)
	print (current_date,current_time)
	return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(1))



#### cliniton route
@app.route("/Home/Clinition", methods = ["GET","POST"])
def c_home():
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	elif session.get('usertype') != 'Admin':
		return "ERROR - Permission required"

	return render_template("Clinition.html", patients = get_all_patients())

def get_all_patients():
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("""SELECT patients.patientID,patients.patientName
	FROM FormSubmissions
	INNER JOIN patients ON patients.patientID = FormSubmissions.patientID
	WHERE FormSubmissions.completed = 'True'""")
	all_patients = cur.fetchall()

	print("PATIENDS",all_patients)
	all_patients = list(set(all_patients))
	print(all_patients)
	all_patients = sorted(all_patients, key=lambda x: x[1])
	print(all_patients)
	conn.close()
	return all_patients

@app.route("/View/<int:user_id>")
def user(user_id):
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	print("HEY")
	print(user_id)
	# Gets the date/time time the form was submitted with the id for the specific patient
	cur.execute("SELECT FormSubmissions.dateCreated, FormSubmissions.id FROM FormSubmissions WHERE patientID = ?",(user_id,))
	date_time = cur.fetchone()
	# Gets all of the results for that one submisson (put in differnt app route)
	cur.execute("""SELECT QuestionTypes.questionType,Questions.questionType, Results.questionID, Results.optionID, Results.optionValue, Results.textField, FormSubmissions.dateCreated
	FROM Results INNER JOIN FormSubmissions ON Results.patientID = FormSubmissions.patientID
	INNER JOIN Questions ON Questions.questionID = Results.questionID
	INNER JOIN QuestionTypes ON QuestionTypes.typeID = Questions.questionType
	WHERE FormSubmissions.completed = "True" AND Results.patientID = ?;""",(user_id,))
	# Gets the date created and completed forms from a specific patient
	cur.execute("SELECT patientName FROM Patients WHERE patientID = ?", (user_id,))
	name = cur.fetchone()[0]
	cur.execute("SELECT dateCreated, id, totalScores FROM FormSubmissions WHERE patientID = ? AND completed = 'True'", (user_id,))
	submissions_by_patient = cur.fetchall()
	print(submissions_by_patient)

	print(f"Date is {date_time[0]} and time was {date_time[1]}")

	return render_template("Patient-Submissions.html", submissions = submissions_by_patient, user_id = user_id, Name =name)


@app.route("/View/<int:user_id>/<int:form_id>")
def show_form(user_id,form_id):
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	print("THIS IS BEING USED")
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	# cur.execute("""SELECT QuestionTypes.questionType,Questions.questionType, Results.questionID, Results.optionID, Results.optionValue, Results.textField, FormSubmissions.dateCreated
	# FROM Results INNER JOIN FormSubmissions ON Results.patientID = FormSubmissions.patientID
	# INNER JOIN Questions ON Questions.questionID = Results.questionID
	# INNER JOIN QuestionTypes ON QuestionTypes.typeID = Questions.questionType
	# WHERE FormSubmissions.completed = "True" AND FormSubmissions.id = ? AND Results.patientID = ?;""",(form_id,user_id,))
	cur.execute("""SELECT QuestionTypes.questionType, Questions.question, Results.questionID, Results.optionID, Results.textField
	FROM Results INNER JOIN FormSubmissions ON Results.patientID = FormSubmissions.patientID AND Results.form_id = FormSubmissions.id
	INNER JOIN Questions ON Questions.questionID = Results.questionID
	INNER JOIN QuestionTypes ON QuestionTypes.typeID = Questions.questionType

	WHERE FormSubmissions.completed = "True" AND FormSubmissions.id = ? AND Results.patientID = ?
	ORDER BY Results.questionID;""",(form_id,user_id,))

	results = cur.fetchall()
	results = [list(elem) for elem in results]
	options_list = [item[3] for item in results]
	option_texts = []
	for options in options_list:

		print("WHATS GOING ON", options)
		split_options = options.split(",")
		print("AFTER SPLIT", split_options)
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		if len(split_options)>1:
			values = []
			for option_id in split_options:
				print("OPTSOIN", option_id)
				cur.execute("SELECT optionText FROM Options WHERE optionID = ?", (option_id,))
				option_text = cur.fetchone()[0]
				print("FETCHED",option_text)
				values.append(option_text)

			option_texts.append(values)
			print("multiple")
		else:
			cur.execute("SELECT optionText FROM Options WHERE optionID = ?", (split_options[0],))
			option_text = cur.fetchone()[0]
			option_texts.append(option_text)
	print("FINALLY",option_texts)
	print("BEFORE INSERTS",results)
	for x in range (0, len(results)):
		results[x][3] = option_texts[x]
	print(results)
	# print("LIST LIST", options_list)
	print(user_id,form_id)
	return render_template("Submission.html", form_results = results)

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
