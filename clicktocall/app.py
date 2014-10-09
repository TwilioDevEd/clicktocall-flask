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

# Declare Twilio client to use for app.
app.client = TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'],
                              app.config['TWILIO_AUTH_TOKEN'])


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

    try:
        app.client.calls.create(from_=app.config['TWILIO_CALLER_ID'],
                                to=phone_number,
                                url=url_for('.outbound', _external=True))
    except Exception as e:
        app.logger.error(e)
        return jsonify({'error': str(e)})

    return jsonify({'message': 'Call incoming!'})


@app.route('/outbound', methods=['POST'])
def outbound():
    response = twiml.Response()

    response.say("Thank you for contacting our sales department. If this "
                 "click to call application was in production, we would "
                 "dial out to your sales team with the Dial verb.",
                 voice='alice')
    '''
    # Uncomment this code and replace the number with the number you want your
    # customers to call.
    with response.dial() as dial:
        dial.number("+16518675309")
    '''
    return str(response)
