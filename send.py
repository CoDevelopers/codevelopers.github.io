import smtplib
print("BEGIN")
session = smtplib.SMTP('smtp.gmail.com:',587)
session.ehlo()
session.starttls()
session.login('abhishyant@gmail.com','xenon2010')
content = "HEllo WOrLD"
session.sendmail('abhishyant@gmail.com','katgstudios@gmail.com',content)
session.quit()
print("SUCCES")