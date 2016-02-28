import smtplib
sender="piushanandismite@gmail.com"
receivers=['piyushanandismite@gmail.com']
message="hi"
try:
	smptpObj=smtplib.SMTP('smtp.gmail.com',587)
	print "ready"
	smptpObj.starttls()
	smptpObj.login("piyushanandismite@gmail.com","***PASSWORD***")
	smptpObj.sendmail(sender,receivers,message)
	print "email sent"
except smtplib.SMTPException:
	print "sending failed"