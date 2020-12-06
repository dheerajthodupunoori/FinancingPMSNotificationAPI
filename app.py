import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "NotificationAPI For FinancingPMS"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


### end swagger specific ###


@app.route("/")
def welcome():
    return jsonify(message="Welcome to Notification API!")


@app.route("/SendEmailNotification", methods=['POST'])
def SendEmailNotification():
    # print(request.get_json()['Subject'])

    mailData = request.get_json()

    sender_address = "notification.personal.dev@gmail.com"
    pwd = "notification@1921"
    receiver_address = "dheeraj.thodupunoori01@gmail.com"

    mail_content = mailData['Body']
    # preparing message
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = mailData['Subject']
    message.attach(MIMEText(mail_content, 'plain'))

    # creating SMTP session
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, pwd)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    return jsonify(mailsentstatus=True)


@app.route('/Parameters')
def VerifyParameters():
    parameter1 = request.args.get("parameter1")
    parameter2 = request.args.get("parameter2")

    return jsonify(parameter1=parameter1, parameter2=parameter2)


@app.route('/urlVariables/<string:parameter1>/<int:parameter2>')
def VerifyURLParameters(parameter1: str, parameter2: int):
    # parameter1 = request.args.get("parameter1")
    # parameter2 = request.args.get("parameter2")
    return jsonify(parameter1=parameter1, parameter2=parameter2)


if __name__ == '__main__':
    app.run()
