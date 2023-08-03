import csv
import smtplib
import ssl

def send_custom_emails():

    sender_email = 'aggiecodingclub.events@gmail.com'
    app_password = 'redactedapppassword'

    #gmail SMTP configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    #SSL/TLS context
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        #TLS encryption
        server.starttls(context=context)

        #login
        server.login(sender_email, app_password)

        #read emails and names from CSV
        with open('emails.csv', 'r') as file: #has to be in the same directory as the script, called emails.csv
            reader = csv.reader(file)
            next(reader)  #skip header row

            #iterate over the rows in the CSV
            for row in reader:
                name = row[0] #first row in the csv
                email = row[1] #second rovw in the csv 

                #email
                subject = f"Hello, {name}!"
                body = f"Dear {name},\n\nThis is a custom email addressed to you."

                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(sender_email, email, message)

    print("Emails sent successfully!")

send_custom_emails()