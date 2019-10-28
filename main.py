from flask import Flask, request, jsonify
from flask_cors import CORS

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config

# Initialize flask app
app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=["POST"])
def send_email_to_ayguen():
    json = request.get_json()
    print(json)
    text = "Name: "  + json['name'] + "\n" + "Mail: " +  json['mail'] + "\n" + "Phone number: " +  json['phone-number'] + "\n" + "Message: "  + json['message'] 

    b = send_email(text)

    return jsonify({"success": b})

def send_email(text):
    mail = MIMEMultipart("alternative")
    mail["SUBJECT"] = "Mail from contact form"
    mail["FROM"]    = config.SMTP_USER
    mail["TO"]      = config.RECEIVER

    text = text

    mail.attach(MIMEText(text, "plain"))

    try:
        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        
        if (config.SMTP_STARTTLS):
            server.starttls()

        server.login(config.SMTP_USER, config.SMTP_PASSWORD)
        server.send_message(mail)
        server.quit()
        return True
    except ConnectionRefusedError:
        print("smtp refused connection")
        return False

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
