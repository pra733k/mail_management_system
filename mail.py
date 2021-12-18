from flask import Flask, redirect, render_template, request, session, abort, flash , Response, request
from flask_wtf import FlaskForm
from form import SignUpForm
from flask import *
import smtplib
import re

app = Flask(__name__, template_folder='templates')
app.config['SECTERT_KEY']='mysecretkey'
s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
s.starttls() # start TLS for security

@app.route("/", methods=['GET','POST'])
def login():
	form = SignUpForm()
	if form.is_submitted():
		sid = request.form()

	if request.method == "POST":
		sid = request.form.get("sid")
	# if(re.search('@gmail.com$', str(sid))):
		return render_template("sid.html",sid = sid)
	else :
		flash('ID NOT ACCEPTED')
		redirect("/") #redirect to login page 
	
	# spass = request.form.get('spass')
	# try:
	# 	s.login(sid, spass) # Authentication - Enter Sender Id & Password
	# 	flash('ID & PASS ACCEPTED')
	# 	return redirect('www.google.com')
	# except Exception as e:
	# 	return Response('Error: {}'.format(str(e)), status=500)
	# return Response(result, status=200)


if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.run(debug=True)