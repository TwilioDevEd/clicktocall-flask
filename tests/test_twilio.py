import unittest
from mock import patch

from twilio.exceptions import TwilioException

from .context import app


app.config['TWILIO_ACCOUNT_SID'] = 'ACxxxxxx'
app.config['TWILIO_AUTH_TOKEN'] = 'yyyyyyyyy'
app.config['TWILIO_CALLER_ID'] = '+15558675309'


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

    @patch('twilio.rest.resources.Calls')
    @patch('twilio.rest.resources.Call')
    def test_call(self, MockCall, MockCalls):
        mock_call = MockCall.return_value
        app.client.calls = MockCalls.return_value
        app.client.calls.create = mock_call

        response = self.app.post('/call',
                                 data={'phoneNumber': '+15556667777'})

        self.assertEquals("200 OK", response.status)

        c = app.client.calls.create
        c.assert_called_once_with(from_=app.config['TWILIO_CALLER_ID'],
                                  to='+15556667777',
                                  url='http://localhost/outbound')

    @patch('twilio.rest.resources.Calls')
    def test_call_error_handling(self, MockCalls):
        def raiseException(*args, **kwargs):
            raise TwilioException("Test error.")
        app.client.calls = MockCalls.return_value
        app.client.calls.create.side_effect = raiseException

        response = self.app.post('/call',
                                 data={'phoneNumber': '+15556667777'})

        self.assertEquals("200 OK", response.status)
        self.assertTrue(b"Test error" in response.data, "Could not "
                        "find error passed through to JSON result: "
                        "{0}".format(response.data))
