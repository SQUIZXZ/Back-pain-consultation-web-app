import os
from flask import Flask, redirect, request, render_template, make_response, escape, session, url_for, flash
import sqlite3

DATABASE = "BACKonLINE.db"
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
questionID = 1
app = Flask(__name__)
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/", methods = ["GET","POST"])
def show_home():
	return redirect(url_for('static', filename='Login.html'))
# @app.route("/login", methods = ["GET","POST"])
# def login():
# 	if request.method == "POST":
# 		print("acualy working")
# 		username = request.form["username"]
# 		password = request.form["password"]


@app.route("/getquestion/<int:form_id>", methods =["GET", "POST"])

def getquestion(form_id):
	global questionID
	options_list, question, questionNum, template = return_question()
	attemptNumber = 1


	# resp.set_cookie('questionID', '1')
	if request.method == "POST":
		if "Next" in request.form:
			hey = request.args.get("question-options")
			#print(hey)
			test1 = request.form["option"]
			#print("TES",test1)
			hey1 = request.args.get("option")
			#print("es",hey1)
			question_result = request.form.getlist("option")

			# for result in question_result:
			# 	if result == "":
			# 		pass
			# 	else:
			# 		print(f"{result} has a value of {return_from_db(result,questionID)[0]}")
			# 	#print(f"{result} has a value of {return_from_db(result)[0]}")

			writethings( question_result,questionNum,attemptNumber, form_id)
			questionID = questionID + 1
			options_list, question, questionNum, template = return_question()
			#print("increment")

			#resp.set_cookie('questionID', str(questionID))
			#return resp
		elif "Back" in request.form:
			#print("back pressed")
			questionID = questionID - 1
			options_list, question, questionNum, template = return_question()
			#print("decrement")
			#resp.set_cookie('questionID', str(questionID))
			#return resp
	resp = make_response(render_template(template, name = "Humzah", question = question[0], options = options_list, questionNum = questionNum))
	return resp
def writethings(question_result,question_number,attemptNumber, form_id):
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
		print(f"before insert Q:{question_number[0]} Option ID: {option_ids} Text: {text} Option Values:{values} Attempt: {attemptNumber} ")
		cur.execute("INSERT INTO Results ('patientID', 'questionID', 'optionID', 'optionValue', 'textField','formID') VALUES (?,?,?,?,?,?)",(39,question_number[0],option_ids,values,text,attemptNumber,form_id))
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
	print("LIST OF OPTIONS FOR QUESTION",options_list)
	return options_list, question, questionNum, template

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
		username = request.form.get('username', default = "Error")
		password = request.form.get('password', default = "Error")
		print(username,password)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			print("BEFORE")
			cur.execute("SELECT EXISTS(SELECT 1 FROM Patients WHERE (patientName = ? AND Password=?))",(username,password,))
			print("AFTER")
			patient_exists = cur.fetchone()
			print("BEFORE")
			cur.execute("SELECT EXISTS(SELECT 1 FROM Clinitions WHERE (clinitionName = ? AND Password=?))",(username,password,))
			print("AFTER")
			clinition_exists = cur.fetchone()
			print("FETCHED")
			cur.close()
			session['logged_in'] = True
			session['username'] = request.form['username']
			# cur.execute("SELECT EXISTS(SELECT 1 FROM Patients WHERE (patientName =? AND Email=?))",(username,password,))
		except:
			print("SOMETHING WENT WRONG")
		if patient_exists[0] == 1:
			return redirect("Home/Patient")
		elif clinition_exists[0] == 1:
			return redirect("Home/Clinition")
		else:
			return redirect("/Login")

	return render_template('Login.html', msg='')

@app.route('/logout')
def logout():
   session.pop('logged_in', None)
   flash("You were logged out")
   return redirect(url_for('login'))

def checkCredentials(uName, pw):
	return pw == 'BACKonLINE'

app.secret_key = ' abc123def456ghi789'
##### patient route
@app.route("/Home/Patient", methods = ["GET"])
def p_home():
	return render_template("Patient.html")


#### cliniton route
@app.route("/Home/Clinition", methods = ["GET","POST"])
def c_home():


	return render_template("Clinition.html", patients = get_all_patients())
def get_all_patients():
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("SELECT patients.patientID,patients.patientName FROM FormSubmissions INNER JOIN patients ON patients.patientID = FormSubmissions.patientID WHERE FormSubmissions.completed = 'True'")
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
	cur.execute("SELECT dateCreated, id FROM FormSubmissions WHERE patientID = ? AND completed = 'True'", (user_id,))
	submissions_by_patient = cur.fetchall()
	print(submissions_by_patient)
	print(f"Date is {date_time[0]} and time was {date_time[1]}")

	return render_template("Patient-Submissions.html", submissions = submissions_by_patient, user_id = user_id)


@app.route("/View/<int:user_id>/<int:form_id>")
def show_form(user_id,form_id):
	print("THIS IS BEING USED")
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	cur.execute("""SELECT QuestionTypes.questionType,Questions.questionType, Results.questionID, Results.optionID, Results.optionValue, Results.textField, FormSubmissions.dateCreated
	FROM Results INNER JOIN FormSubmissions ON Results.patientID = FormSubmissions.patientID
	INNER JOIN Questions ON Questions.questionID = Results.questionID
	INNER JOIN QuestionTypes ON QuestionTypes.typeID = Questions.questionType
	WHERE FormSubmissions.completed = "True" AND FormSubmissions.id = ? AND Results.patientID = ?;""",(form_id,user_id,))
	results = cur.fetchall()
	print(results)
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
