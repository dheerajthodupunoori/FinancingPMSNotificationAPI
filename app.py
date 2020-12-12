from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from scripts.notification import sendEmail

app = Flask(__name__)

# swagger specific
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


# end swagger specific


@app.route("/")
def welcome():
    return jsonify(message="Welcome to Notification API!")


@app.route("/SendEmailNotification", methods=['POST'])
def SendEmailNotification():
    mailData = request.get_json()
    try:
        sendEmail(mailData)
    except Exception as e:
        print("An error occurred while sending an email.")
        print(e)
        return "False"
    # else block executed only when try does not throw any exception
    else:
        print("Email sent successfully")
    # finally block is executed only when
    finally:
        print("Email process completed")

    return "True"


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
