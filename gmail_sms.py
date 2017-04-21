#!/usr/bin python
# -*- coding: utf-8 -*-

import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TO = "<CELLULAR CARRIER EMAIL>" # should begin with your 9 digit number
CLIENT = "<GMAIL ADDRESS>"
CLIENT_PSWD = "<GOOGLE A/C APP PSWD>" # if no 2-factor auth, use normal pswd


def send_text():
	msg = MIMEMultipart()
	msg['From'] = CLIENT
	msg['To'] = TO
	msg['Subject'] = "UDACITY REVIEWS"
	body = "You have been assigned to grade a new submission!  "
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(CLIENT, CLIENT_PSWD)

	text = msg.as_string()
	server.sendmail(CLIENT, TO, text)
	time.sleep(1)
	server.quit()