from flask import Flask, render_template, url_for, request, session, redirect
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

client = MongoClient('localhost')
client.school.authenticate('first','first')

print ('client')

@app.route("/")
def main():
	return render_template('project.html')

@app.route('/project', methods = ['POST'])
def project():
	if request.method == 'POST':
		db = client['school']
		col = db['students']
		es = col.find_one({"Roll_No" : request.form["roll_no"], "Subject_Code" : request.form["sub_code"]})
		if es is None:
			dist = ({"Name" : request.form["name"], "Roll_No" : request.form["roll_no"], "Semester" : request.form["sem"], "Subject_Code" : request.form["sub_code"], "Lecture_Quality" : request.form["lec"], "Assignment_Quality" : request.form["assign"], "Any Comment" : request.form["otherText"]})
			col.insert_one(dist)
			print(request.form["name"])
			print(request.form["roll_no"])
			print(request.form["sem"])
			print(request.form["sub_code"])
			print(request.form["lec"])
			print(request.form["assign"])
			print(request.form["otherText"])
			return render_template("submit.html")
		else:
			return render_template("exist.html")
	
if __name__ == '__main__':
   app.run(debug = True)
