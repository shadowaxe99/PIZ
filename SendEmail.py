```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email, deck):
    # setup the parameters of the message
    password = "your_password"
    msg = MIMEMultipart()
    msg['From'] = "your_email"
    msg['To'] = email
    msg['Subject'] = "Deck Information"

    # add in the message body
    msg.attach(MIMEText(deck, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))
    return "Capture Response"
```