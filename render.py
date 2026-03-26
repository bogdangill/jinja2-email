# First let's get jinja2
from jinja2 import Template

import os
import json

# We will need smtplib to connect to our smtp email server
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Add dotenv to use environment dictionary
from dotenv import load_dotenv
load_dotenv()

# Read the Jinja2 email template
with open("templates/template.html", "r") as file:
    template_str = file.read()

with open('texts.json', 'r', encoding='utf-8') as f:
    all_texts = json.load(f)

jinja_template = Template(template_str)

# Add essential data via env vars to login to server
EMAIL_ADDRESS = os.environ.get("MAIL_SENDER")
EMAIL_PASS = os.environ.get("MAIL_PASS")
R_GMAIL = os.environ.get("RECIPIENT_GMAIL")
G_MAILRU = os.environ.get("RECIPIENT_MAILRU")

# Define email server and credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Set up email server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASS)
except Exception as e:
    print(f"Error: {e}")

# Define recipients and their details
# This can be read from some CSV file or passed from some other program or API
people_data = [
    {"name": "Pocik1", "email": R_GMAIL},
    {"name": "Pocik2", "email": G_MAILRU}
]

# Now we iterate over our data to generate and send custom emails to each
for person in people_data:
    email_content = jinja_template.render(all_texts)

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = person["email"]
    msg["Subject"] = all_texts["subject"]

    # Attach the HTML content to the email
    msg.attach(MIMEText(email_content, "html"))

    # Print and send the email
    print(f"Sending email to {person['email']}")
    
    server.sendmail(EMAIL_ADDRESS, person["email"], msg.as_string())
    print("Email has been sent successfully!\n")

# Close the server connection
server.quit()