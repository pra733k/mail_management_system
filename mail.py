import flask
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
s.starttls() # start TLS for security

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = base_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


sid = input('Enter Sender Email Id: ')
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

if __name__ == "__main__":
	app.run(use_reloader=True, debug=True)