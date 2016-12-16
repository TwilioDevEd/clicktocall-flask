from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for

from twilio import twiml
from twilio.rest import TwilioRestClient

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')


# Route for Click to Call demo page.
@app.route('/')
def index():
    return render_template('index.html',
                           configuration_error=None)


# Voice Request URL
@app.route('/call', methods=['POST'])
def call():
    # Get phone number we need to call
    phone_number = request.form.get('phoneNumber', None)
    sales_number = request.form.get('salesNumber', None)

    try:
        twilio_client = TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'],
                                         app.config['TWILIO_AUTH_TOKEN'])
    except Exception as e:
        msg = 'Missing configuration variable: {0}'.format(e)
        return jsonify({'error': msg})

    try:
        twilio_client.calls.create(from_=app.config['TWILIO_PHONE'],
                                   to=phone_number,
                                   url=url_for('.outbound',
                                               _external=True,
                                               salesNumber=sales_number))
    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': str(e)})

    return jsonify({'message': 'Call incoming!'})


@app.route('/outbound/<salesNumber>', methods=['POST'])
def outbound(salesNumber):
    response = twiml.Response()

    response.say("Thanks for contacting our sales department. Our next"
                 "available representative will take your call.",
                 voice='alice')

    with response.dial() as dial:
        dial.number(salesNumber)

    return str(response)


# Route for Landing Page after Heroku deploy.
@app.route('/landing.html')
def landing():
    return render_template('landing.html',
                           configuration_error=None)
