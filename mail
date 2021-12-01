# Python code to illustrate Sending mail
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
s.starttls() # start TLS for security
# sid = input('Enter Sender Email Id: ')
# spass = input('Enter Sender Email Password: ')
s.login("18bec045@smvdu.ac.in", "prateek0690") # Authentication - Enter Sender Id & Password
rid = input("Enter receiver Id: ")
subject = input("Enter your subject here: ")
message = input("Enter your message here: ")
msg = f'Subject: {subject}\n\n{message}'
s.sendmail("18bec045@smvdu.ac.in", rid, msg) # sending the mail
s.quit()  # terminating the session
