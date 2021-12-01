# Python code to illustrate Sending mail
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
s.starttls() # start TLS for security
# sid = input('Enter Sender Email Id: ')
# spass = input('Enter Sender Email Password: ')
s.login("18bec045@smvdu.ac.in", "prateek0690") # Authentication - Enter Sender Id & Password
subject = input("Enter your subject here: ")
message = input("Enter your message here: ")
msg = f'Subject: {subject}\n\n{message}'
lirec=[]
x = int(input("Enter no. of recipients: "))
for k in range(x):
	rid = input("Enter receiver Id: ")
	lirec.append(rid)
for i in lirec:
	s.sendmail("18bec045@smvdu.ac.in", i, msg) # sending the mail
s.quit()  # terminating the session