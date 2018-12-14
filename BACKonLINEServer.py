import os
from flask import Flask, redirect, request, render_template, make_response, escape, session, url_for, flash
import sqlite3
from datetime import datetime
import time
from functools import wraps

DATABASE = "BACKonLINE.db"

app = Flask(__name__)
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# Redirects to the Login page when the ip is entered
@app.route("/", methods = ["GET","POST"])
def show_home():
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	return redirect("Login")

# App route for getting questions
@app.route("/getquestion/<int:patient_id>/<int:form_id>/<int:question_number>", methods =["GET", "POST"])
# Main code for going to next and going back questions
def getquestion(form_id,patient_id,question_number):
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	elif session.get('usertype') != 'Patient':
		return "ERROR - Permission required"

	# global questionID
	print("CURRENT QUETSOPN", question_number)
	options_list, question, questionNum, template, option_texts, fetched_texts = return_question(question_number,patient_id,form_id)
	print("FETHCED ££££", option_texts, fetched_texts)

	# resp.set_cookie('questionID', '1')
	if request.method == "POST":
		if "Next" in request.form:
			question_result = request.form.getlist("option")
			writethings(patient_id, question_result,questionNum, form_id)
			# questionID = questionID + 1
			question_number += 1
			if question_number > 39:
				question_number = 39
				return redirect("submit_assessment/"+str(patient_id)+"/"+str(form_id))
			# options_list, question, questionNum, template = return_question(question_number,patient_id,form_id)
			#print("increment")
			return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(question_number))


		elif "Back" in request.form:

			question_number -= 1
			if question_number == 0:
				question_number = 1

			return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(question_number))
	resp = make_response(render_template(template, name = "Humzah", question = question[0], options = options_list, questionNum = questionNum, id = patient_id, selected_options = option_texts, selected_texts =fetched_texts  ))
	return resp
# Function used to write the user options selected into the DB
def writethings(patient_id,question_result,question_number, form_id):
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
		print('rollback')
		msg = "An error has occured"
	finally:
		conn.close()

		print('finllay')
		print(msg)
		return msg

# Used to check if the quesion already exists inside the DB, used for selected
# Option Persistecy in questions
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
# Function returns all the necessary information needed to display the question
# Also returns the question type so the program knows what templates to use for
# the question
def return_question(question_number,patient_id,form_id):
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		# These get the questionID, questionnumber and options for the questions
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
	# Returns true if the question already exists in the DB and False for the latter
	returned_bool = check_if_form_question_exists(form_id,question_number)
	print("RETURNED BOOL FOR PERSISTENCY",returned_bool)
	# If the question already exists then we need to get the options that was
	# previously selected
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
					# Gets the actual text of the options that was selected
					# by querying the id of the option
					cur.execute("SELECT optionText FROM Options WHERE optionID = ?",(int(item),))
					option_texts.append(cur.fetchone()[0])

				except:
					conn.rollback()
					print("ROLLING FROM inside question")
				finally:
					pass
			print("££££££££££££", fetched_texts)
			print("LISTED ggrgr")

		except:
			conn.rollback()
			print("ROLLING FROM return question")
		finally:
			cur.close()
		print(option_texts, fetched_texts)
		# Splits the text to ":" which can be split later
		# "," delimter was not used as it caused issues with optoins with commas
		fetched_texts = ':'.join(fetched_texts)
		option_texts = ':'.join(option_texts)
		print("£$%£$%^&%&&^%&%", fetched_texts, option_texts)

	# If the question doesn't exist in the DB for the form then the program just
	# gives an empty options as nothing is selected
	else:
		print("The row doens't exist in the results",question_number)
		option_texts =[]
		fetched_texts = []
	# Conditions to choose a template to use to view each question
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
	# Returns the base options for the questions, the question number, the text
	# for the question, the template to use and any previousoly selected options/texts
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

	except:
		conn.rollback()
		print("rollback")
		msg = "error"
	finally:
		conn.close()
	returning_value = str(total_score) +"/" +str(max_score)
	print("WOAH",returning_value)
	return returning_value

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
			return "Something went wrong, please try again"
		finally:
			conn.close()
		print(msg)
		return msg
# App route to log the user in
@app.route("/Login", methods = ['GET', 'POST'])
def login():
	# Session validation to check if a user should be able to access this page

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
# App route used to log the user out
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
# App route for the Patients Home Page
@app.route("/Home/Patient/<int:id>", methods = ["GET"])
def p_home(id):
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	elif session.get('usertype') != 'Patient':
		return "ERROR - Permission required"
	# When a patient logs in, the program checks whether there are assessments
	# past 24 hours for that user in the DB
	delete_any_old_assessments(id)
	try:
		conn = sqlite3.connect(DATABASE)
		print("connected")
		cur = conn.cursor()
		print("cursor")
		# Fetches the patient details from the DB
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
# This fucntion deletes any assessment that is over 24 hours of age
def delete_any_old_assessments(id):
	try:
		conn = sqlite3.connect(DATABASE)
		print("connected")
		cur = conn.cursor()
		print("cursor")
		# Fetches all of the date of the forms that the user has
		cur.execute("SELECT id, dateCreated FROM FormSubmissions WHERE patientID = ? AND completed = 'False';",(int(id),))
		print("selected")
		fetched_forms = cur.fetchall()
		print("fetched",fetched_forms)
	except:
		conn.rollback()
		print("rollback")
	finally:
		conn.close()
	# puts the list of tuples into a list of lists
	fetched_forms = map(list, fetched_forms)
	# iterate through all the forms to cehck if the current date and time is in 24 hours
	for form in fetched_forms:
		form_id = form[0]
		print("ID",int(form_id))
		print(form)
		stringed_date_time = form[1].split(",")
		stringed_date = stringed_date_time[0].split("-")
		stringed_time = stringed_date_time[1].split(":")
		# Puts the fetched date and time in a useable format
		past_date = datetime(int(stringed_date[2]),int(stringed_date[1]),int(stringed_date[0]),int(stringed_time[0]),int(stringed_time[1]),int(stringed_time[2]),int(stringed_time[3]))
		print(stringed_date,stringed_time)

		print(past_date)
		# Gets the current date
		difference = datetime.utcnow() - past_date
		print(difference)
		# If the difference is over 1 then it is more than 24 hours
		# Otherwise it is still within 24hours
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
		# Delets the rows form the Results and FormSubmissions
		# corresponding to the form id passed
		cur.execute("DELETE FROM Results WHERE form_id = ?",(id,))
		cur.execute("DELETE FROM FormSubmissions WHERE id = ?",(id,))
		conn.commit()
		print("delete complete")
	except:
		conn.rollback()
		print("rollback")
	finally:
		conn.close()

# App route to direct the user to a edit submission page
@app.route("/Home/Patient/<int:user_id>/Edit_Submissions")
def edit_submissions(user_id):
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()

		# Gets all the forms where the form isn't complete
		cur.execute("SELECT dateCreated, id FROM FormSubmissions WHERE patientID = ? AND completed = 'False'", (user_id,))
		submissions_by_patient = cur.fetchall()
		print(submissions_by_patient)

	except:
		conn.rollback()
		print("rollback 123456346")
		submissions_by_patient = []


	return render_template("Edit_Submissions.html", submissions = submissions_by_patient, user_id = user_id)
# App route for when a patient wants to edit a submission
@app.route("/edit_submission/<int:patient_id>/<int:form_id>")
def edit_form(patient_id,form_id):
	print("pateinte",patient_id, "form",form_id)
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		print("1")
		# Fetches the last question ID that was answered and this inserted into the Results table
		# for that specific user and form id
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
	# If the query search gets a None then go to question 1 as there is nothing in the DB
	# yet for the form
	if fetched_question_number == None:
		fetched_question_number = 1
	return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(fetched_question_number))

# App route for when a new assessment is created
@app.route("/New-Assessment/<int:patient_id>")
def new_surver(patient_id):
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	print("USER_ID", patient_id)
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	# Used to find the current date and time
	i = datetime.now()
	# gets the date in a string form
	current_date = i.strftime("%d-%m-%Y")
	# split them into list elements so it is easier to edit
	stringed_date = current_date.split("-")
	# gets the time in a string form
	current_time = i.strftime("%H:%M:%S:%f")
	# split them into list elements so it is easier to edit
	stringed_time = current_time.split(":")
	# joings the two date and time strings together
	stringed_date_time = current_date + "," + current_time
	# Inserts the id, completed status and date the form was created into the table
	cur.execute("INSERT INTO FormSubmissions (patientID, completed, dateCreated,dateSubmitted,totalScores) VALUES (?,?,?,?,?)",(patient_id,'False',stringed_date_time," "," ",))
	print("DATE-TIME", current_date + "," + current_time,stringed_date_time)
	form_id = cur.lastrowid
	conn.commit()
	conn.close()
	# print("FORM ID", form_id)
	# past_date = datetime(int(stringed_date[2]),int(stringed_date[1]),int(stringed_date[0]),int(stringed_time[0]),int(stringed_time[1]),int(stringed_time[2]),int(stringed_time[3]))
	#
	# difference = datetime.utcnow() - past_date
	# if (difference.days == 0):
	# 	msg = "Date is within 24 hours"
	#
	# else:
	# 	msg = "You can no longer edit this submisssion"
	# print("TIME DIFFERENCE", difference)
	# print(i,past_date)
	# print(msg)
	# print (current_date,current_time)
	return redirect("getquestion/"+str(patient_id)+"/"+str(form_id)+"/"+str(1))



# App route for the Admin/Clinition page
# Where they can see all of the patient submissions
@app.route("/Home/Clinition", methods = ["GET","POST"])
def c_home():
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))
	elif session.get('usertype') != 'Admin':
		return "ERROR - Permission required"
	return render_template("Clinition.html", patients = get_all_patients())
# Function gets all of the patients that have submitted an Assessment
# Then sorts them in acesding order alphabetcically
def get_all_patients():
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	# Fetches the patient ID, patient Name from the DB where a form
	# is complete
	cur.execute("""SELECT patients.patientID,patients.patientName
	FROM FormSubmissions
	INNER JOIN patients ON patients.patientID = FormSubmissions.patientID
	WHERE FormSubmissions.completed = 'True'""")
	all_patients = cur.fetchall()

	print("PATIENDS",all_patients)
	# Sets the list so there are no duplicate patient anmes
	all_patients = list(set(all_patients))
	print(all_patients)
	# Sorts the list aplhabetically
	all_patients = sorted(all_patients, key=lambda x: x[1])
	print(all_patients)
	conn.close()
	return all_patients
# App route to view a specific patient's submissions as a talbe
@app.route("/View/<int:user_id>")
def user(user_id):
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	# Fetches the date/time the form was submitted
	cur.execute("SELECT FormSubmissions.dateCreated, FormSubmissions.id FROM FormSubmissions WHERE patientID = ?",(user_id,))
	date_time = cur.fetchone()
	# Fetches the patient name from the DB
	cur.execute("SELECT patientName FROM Patients WHERE patientID = ?", (user_id,))
	name = cur.fetchone()[0]
	# Fetches the date created
	cur.execute("SELECT dateSubmitted, id, totalScores FROM FormSubmissions WHERE patientID = ? AND completed = 'True'", (user_id,))
	submissions_by_patient = cur.fetchall()
	print(submissions_by_patient)

	print(f"Date is {date_time[0]} and time was {date_time[1]}")

	return render_template("Patient-Submissions.html", submissions = submissions_by_patient, user_id = user_id, Name =name)

# App route used to View a specific form from a specific patient
# Takes in the patient's id and the form id as parameters from the URL
@app.route("/View/<int:user_id>/<int:form_id>")
def show_form(user_id,form_id):
	# Session validation to check if a user should be able to access this page
	if not session.get('logged_in') and not session.get('usertype') and not session.get('email'):
		return redirect(url_for('login'))

	print("THIS IS BEING USED")
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	#Fetches the patient name from the db using the id of the patient
	cur.execute("SELECT patientName  FROM Patients WHERE patientID = ?",(int(user_id),))
	patient_name = cur.fetchone()[0]
	# Fetches the question type, question, questionID, optoinsID, text in text-field to show to the admin
	# Used to show all of the question they answered and also the options they chose for the questions
	cur.execute("""SELECT QuestionTypes.questionType, Questions.question, Results.questionID, Results.optionID, Results.textField
	FROM Results INNER JOIN FormSubmissions ON Results.patientID = FormSubmissions.patientID AND Results.form_id = FormSubmissions.id
	INNER JOIN Questions ON Questions.questionID = Results.questionID
	INNER JOIN QuestionTypes ON QuestionTypes.typeID = Questions.questionType
	WHERE FormSubmissions.completed = "True" AND FormSubmissions.id = ? AND Results.patientID = ?
	ORDER BY Results.questionID;""",(form_id,user_id,))

	results = cur.fetchall()
	# Makes a list of tuples in to a list of list
	results = [list(elem) for elem in results]
	# gets the options from the results list as they are in the 4 th element of the sublist
	options_list = [item[3] for item in results]

	option_texts = []
	#Iterate thorugh every option inside the list and find its corrosponding Option text
	for options in options_list:

		print("WHATS GOING ON", options)
		# Split the element just in case there is a list in the item
		split_options = options.split(",")
		print("AFTER SPLIT", split_options)
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		# If the item is a list then you need to go further to find each one
		if len(split_options)>1:
			values = []
			# iterate thourgh the list of the element
			for option_id in split_options:
				print("OPTSOIN", option_id)
				# Gets the option text for the element
				cur.execute("SELECT optionText FROM Options WHERE optionID = ?", (option_id,))
				option_text = cur.fetchone()[0]
				print("FETCHED",option_text)
				# Appends into a separate sublist to that we can refer to it in the same
				# Way as we have saved in the DB when we view the answers
				values.append(option_text)
			# Appends the text into a bigger list
			option_texts.append(values)
			print("multiple")
		else:
			# If there are no sublists in the element then this code is run
			values = []
			# Gets the option text for the element
			cur.execute("SELECT optionText FROM Options WHERE optionID = ?", (split_options[0],))
			option_text = cur.fetchone()[0]
			values.append(option_text)
			# Appends the text into a bigger list
			option_texts.append(values)

	# Puts the option text that was just fetched into the correct positions
	# Replacing the Options ids with the actual text
	for x in range (0, len(results)):
		results[x][3] = option_texts[x]

	return render_template("Submission.html", form_results = results, name = patient_name, formID = form_id)

# App route adds prexisting data which can be used to demo a submission for a patient
@app.route("/add_data_for_submission/<int:patient_id>")
def submitoption(patient_id):
	# Used to find the current date and time
	i = datetime.now()
	# gets the date in a string form
	current_date = i.strftime("%d-%m-%Y")
	# set the date to be a day before
	stringed_date = current_date.split("-")
	# gets the time in a string form
	current_time = i.strftime("%H:%M:%S:%f")
	# split them into list elements so it is easier to edit
	stringed_time = current_time.split(":")
	# joings the two date and time strings together
	stringed_date_time = current_date + "," + current_time
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		# Updates the FormSubmissions table by adding the patient id and the current date to the form id of 1
		# which contains a pre-existing filled out form
		cur.execute("UPDATE FormSubmissions SET patientID = ? ,dateCreated = ? WHERE id =?",(patient_id,stringed_date_time,1))
		# Updates the Results table by changing the patient ID for the form of 1 so that they are linked together
		cur.execute("UPDATE Results SET patientID = ? WHERE form_id = 1", (patient_id,))
		conn.commit()
		print("COMMITED TO DB")
	except:
		conn.rollback()
		print("ILJ")
	finally:
		conn.close()

	return ("ADDING DATA FOR PATIENT" + str(patient_id))
# App route adds a demo for a 24 hour form submission
@app.route("/add_data/24-hour/<int:patient_id>")
def add_24_hour_test_form(patient_id):
	# Code used to set the expiry date of the form
	# to 60 seconds form now
	i = datetime.now()
	# gets the date in a string form
	current_date = i.strftime("%d-%m-%Y")
	# split them into list elements so it is easier to edit
	stringed_date = current_date.split("-")
	# set the date to be a day before
	new_date = int(stringed_date[0]) - 1
	stringed_date[0] = str(new_date)
	print(new_date,stringed_date)

	# gets the time in a string form
	current_time = i.strftime("%H:%M:%S:%f")
	# split them into list elements so it is easier to edit
	stringed_time = current_time.split(":")
	print("ITME",stringed_time)
	# set the minute to be 1 minute ahead
	new_minute = int(stringed_time[1]) + 1
	print(new_minute)
	#check if the new minute is over 60 minutes as then we need to increment the hour
	if (new_minute > 60):
		print("NEED TO REMOVE HOUR")
		new_hour = int(stringed_time[0]) + 1
		stringed_time[1] = "00"
		stringed_time[0] = str(new_hour)
	# if the new minute isn't above 60 then we can continue by just incrementin the minute
	else:
		print("NEED TO REMOVE minutes")
		add_60_seconds = int(stringed_time[1]) + 1
		stringed_time[1] = str(add_60_seconds)
	# joins the date and time lists together using different delimiters
	new_date_string = "-".join(stringed_date)
	new_time_string = ":".join(stringed_time)
	print(new_date_string,new_time_string)
	# joings the two date and time strings together
	stringed_date_time = new_date_string + "," + new_time_string
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		# Inserts the patient ID, sets the completed column to False, adds the current date/time
		# sets the last coloumns to Blank as they are only required for when the form is complete
		cur.execute("INSERT INTO FormSubmissions (patientID, completed, dateCreated,dateSubmitted,totalScores) VALUES (?,?,?,?,?)",(patient_id,'False',stringed_date_time," "," ",))
		form_id = cur.lastrowid
		conn.commit()
		print("SUBMITTED WITH FORM ID", form_id)
	except:
		conn.rollback()
		print("rollback 123456346")
	finally:
		conn.close()
	# returns a message to the page
	return ("ADDING 24 hour submission form for patient: "+ str(patient_id))

# App route to add submission for the Admin page to see in the DEMO
# Manually sets all of the existing forms to True so that they are "complete"
@app.route("/add_submissions")
def add_submission():
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.cursor()
		# Finds the form depedning on its id and then sets a coloumn of completed to True
		cur.execute("UPDATE FormSubmissions SET completed = 'True' WHERE id = 23;")
		cur.execute("UPDATE FormSubmissions SET completed = 'True' WHERE id = 24;")
		cur.execute("UPDATE FormSubmissions SET completed = 'True' WHERE id = 25;")
		cur.execute("UPDATE FormSubmissions SET completed = 'True' WHERE id = 26;")
		cur.execute("UPDATE FormSubmissions SET completed = 'True' WHERE id = 27;")
		cur.execute("UPDATE FormSubmissions SET completed = 'True' WHERE id = 28;")
		conn.commit()
	except:
		conn.rollback()
		print("rollback 123456346")
	finally:
		conn.close()
	# returns a message to the page
	return "Adding Submissions for Patients"

if __name__ == "__main__":
	app.run(debug=True)
