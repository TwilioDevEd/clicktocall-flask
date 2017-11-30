import unittest
from mock import patch

from app import app

app.config['TWILIO_ACCOUNT_SID'] = 'ACxxxxxx'
app.config['TWILIO_AUTH_TOKEN'] = 'yyyyyyyyy'
app.config['TWILIO_CALLER_ID'] = '+15558675309'

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/" \
           "{0}".format(app.config['TWILIO_ACCOUNT_SID'])
AUTH = (app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])


class TwiMLTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def assertTwiML(self, response):
        app.logger.info(response.data)
        self.assertTrue(b"</Response>" in response.data, "Did not find "
                        "</Response>: {0}".format(response.data))
        self.assertEqual("200 OK", response.status)

    def sms(self, body, url='/sms', to=app.config['TWILIO_CALLER_ID'],
            from_='+15558675309', extra_params=None):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': app.config['TWILIO_ACCOUNT_SID'],
            'To': to,
            'From': from_,
            'Body': body,
            'FromCity': 'BROOKLYN',
            'FromState': 'NY',
            'FromCountry': 'US',
            'FromZip': '55555'}
        if extra_params:
            params = dict(params.items() + extra_params.items())
        return self.app.post(url, data=params)

    def call(self, url='/voice', to=app.config['TWILIO_CALLER_ID'],
             from_='+15558675309', digits=None, extra_params=None):
        params = {
            'CallSid': 'CAtesting',
            'AccountSid': app.config['TWILIO_ACCOUNT_SID'],
            'To': to,
            'From': from_,
            'CallStatus': 'ringing',
            'Direction': 'inbound',
            'FromCity': 'BROOKLYN',
            'FromState': 'NY',
            'FromCountry': 'US',
            'FromZip': '55555'}
        if digits:
            params['Digits'] = digits
        if extra_params:
            params = dict(params.items() + extra_params.items())
        return self.app.post(url, data=params)


class ClickToCallTests(TwiMLTest):
    def test_index(self):
        response = self.app.get('/')
        self.assertEquals("200 OK", response.status)

    def test_outbound(self):
        response = self.call(url='/outbound')
        self.assertTwiML(response)

    def test_call(self):
        with patch('twilio.rest.api.v2010.account.call.CallList.create') as mock:  # noqa: E501
            response = self.app.post('/call',
                                     data={'phoneNumber': '+15556667777'})

        # Assert
        self.assertEquals("200 OK", response.status)
        self.assertTrue(mock.called)
        mock.assert_called_with(
            to='+15556667777',
            from_=app.config['TWILIO_CALLER_ID'],
            url='http://localhost/outbound'
        )


class NoCredentialsTests(unittest.TestCase):
    def setUp(self):
        del(app.config['TWILIO_ACCOUNT_SID'])
        self.app = app.test_client()

    def test_call_without_twilio_credentials(self):
        response = self.app.post('/call',
                                 data={'phoneNumber': '+15556667777'})

        self.assertEquals("200 OK", response.status)
        self.assertTrue(b"Missing" in response.data, "Could not "
                        "find error for missing Twilio credentials: "
                        "{0}".format(response.data))
