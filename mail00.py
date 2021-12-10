from flask import Flask
import smtplib
import re

s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
s.starttls() # start TLS for security

app = Flask(__name__, template_folder='templates')


print("Please Enable 'Less secure app access' in your E-mail Account.\n")
sid = input('Enter Sender Email Id: ')

if(re.search('@gmail.com$', sid)):
	print("email check")

	spass = input('Enter Sender Email Password: ')
	s.login(sid, spass) # Authentication - Enter Sender Id & Password

	subject = input("Enter your subject here: ")
	message = input("Enter your message here: ")
	msg = f'Subject: {subject}\n\n{message}'

	lirec=[]
	x = int(input("Enter no. of recipients: "))

	for k in range(x):
		rid = input("Enter receiver Id "+str(k+1)+" : ")
		lirec.append(rid)
	for i in lirec:
		s.sendmail(sid, i, msg) # sending the mail

	s.quit()  # terminating the session

else : 
	print("Email Invalid")
	#redirect to login page 

if __name__ == "__main__":
	app.run(use_reloader=True, debug=True)