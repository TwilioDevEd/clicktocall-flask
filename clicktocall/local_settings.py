import os

'''
Configuration Settings
'''

''' Uncomment to configure using the file.
WARNING: Be careful not to post your account credentials on GitHub.

TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_PHONE = "+17778889999"
'''

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_PHONE = os.environ.get('TWILIO_PHONE', None)
TWILIO_APP_SID = os.environ.get('TWILIO_APP_SID', None)
