import csv
import smtplib
from email.mime.text import MIMEText
from datetime import date, timedelta

# Connect to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

# Login to the email account
server.login('#youremailid@gmail.com#', '#Your Email password#')

# Read the data from the CSV file
with open('birthday.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader) # Skip the first row with the headers
    for row in csv_reader:
        name = row[0]
        email = row[1]
        birthday = row[2]
        birthday_date = date.fromisoformat(birthday)

        # Check if it's the person's birthday today
        today = date.today()
        if birthday_date.month == today.month and birthday_date.day == today.day:
            # Send the birthday email
            message = MIMEText(f'Happy birthday, {name}!')
            message['to'] = email
            message['subject'] = 'Happy birthday! I hope You are doing Great :)'
            server.send_message(message)

# Close the connection to the email server
server.quit()
