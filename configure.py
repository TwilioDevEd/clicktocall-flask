'''
Hackpack Configure
A script to configure your TwiML apps and Twilio phone numbers to use your
hackpack's Heroku app.

Usage:

Auto-configure using your local_settings.py:
    python configure.py

Deploy to new Twilio number and App Sid:
    python configure.py --new

Deploy to specific App Sid:
    python configure.py --app APxxxxxxxxxxxxxx

Deploy to specific Twilio number:
    python configure.py --number +15556667777

Deploy to custom domain:
    python configure.py --domain example.com
'''

from argparse import ArgumentParser
import subprocess
import logging

from twilio.rest import TwilioRestClient
from twilio.exceptions import TwilioException

from clicktocall import local_settings


class Configure(object):
    def __init__(self, account_sid=local_settings.TWILIO_ACCOUNT_SID,
                 auth_token=local_settings.TWILIO_AUTH_TOKEN,
                 app_sid=local_settings.TWILIO_APP_SID,
                 phone_number=local_settings.TWILIO_PHONE,
                 voice_url='/voice',
                 sms_url='/sms',
                 host=None, **kwargs):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.app_sid = app_sid
        self.phone_number = phone_number
        self.host = host
        self.voice_url = voice_url
        self.sms_url = sms_url
        self.friendly_phone_number = None

    def start(self):
        logging.info("Configuring your Twilio hackpack...")
        logging.debug("Checking if credentials are set...")
        if not self.account_sid:
            raise ConfigurationError("ACCOUNT_SID is not set in "
                                     "local_settings.")
        if not self.auth_token:
            raise ConfigurationError("AUTH_TOKEN is not set in "
                                     "local_settings.")

        logging.debug("Creating Twilio client...")
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

        logging.debug("Checking if host is set.")
        if not self.host:
            logging.debug("Hostname is not set...")
            self.host = self.getHerokuHostname()

        # Check if urls are set.
        logging.debug("Checking if all urls are set.")
        if "://" not in self.voice_url:
            self.voice_url = self.host + self.voice_url
            logging.debug("Setting voice_url with host: "
                          "{0}".format(self.voice_url))
        if "://" not in self.sms_url:
            self.sms_url = self.host + self.sms_url
            logging.debug("Setting sms_url with host: {0}".format(self.sms_url))

        if self.configureHackpack(self.voice_url, self.sms_url,
                                  self.app_sid, self.phone_number):

            # Configure Heroku environment variables.
            configuration = {'TWILIO_ACCOUNT_SID': self.account_sid,
                             'TWILIO_AUTH_TOKEN': self.auth_token,
                             'TWILIO_APP_SID': self.app_sid,
                             'TWILIO_PHONE': self.phone_number}
            self.setHerokuEnvironmentVariables(**configuration)

            # Ensure local environment variables are set.
            self.printLocalEnvironmentVariableCommands(**configuration)

            logging.info("Hackpack is now configured.  Call {0} to "
                         "test!".format(self.friendly_phone_number))
        else:
            logging.error("There was an error configuring your hackpack. "
                          "Weak sauce.")

    def configureHackpack(self, voice_url, sms_url, app_sid,
                          phone_number, *args):

        # Check if app sid is configured and available.
        if not app_sid:
            app = self.createNewTwiMLApp(voice_url, sms_url)
        else:
            app = self.setAppRequestUrls(app_sid, voice_url, sms_url)

        # Check if phone_number is set.
        if not phone_number:
            number = self.purchasePhoneNumber()
        else:
            number = self.retrievePhoneNumber(phone_number)

        # Configure phone number to use App Sid.
        logging.info("Setting {0} to use application sid: "
                     "{0}".format(number.friendly_name, app.sid))
        try:
            self.client.phone_numbers.update(number.sid,
                                             voice_application_sid=app.sid,
                                             sms_application_sid=app.sid)
            logging.debug("Number set.")
        except TwilioException as e:
            raise ConfigurationError("An error occurred setting the "
                                     "application sid for "
                                     "{0}: {1}".format(number.friendly_name, e))

        # We're done!
        if number:
            return number
        else:
            raise ConfigurationError("An unknown error occurred configuring "
                                     "request urls for this hackpack.")

    def createNewTwiMLApp(self, voice_url, sms_url):
        logging.debug("Asking user to create new app sid...")
        i = 0
        while True:
            i = i + 1
            choice = raw_input("Your APP_SID is not configured in your "
                               "local_settings.  Create a new one? "
                               "[y/n]").lower()
            if choice == "y":
                try:
                    logging.info("Creating new application...")
                    app = self.client.applications.create(voice_url=voice_url,
                                                          sms_url=sms_url,
                                                          friendly_name="Hack"
                                                                        "pack"
                                                                        " for "
                                                                        "Hero"
                                                                        "ku a"
                                                                        "nd F"
                                                                        "lask")
                    break
                except TwilioException as e:
                    raise ConfigurationError("Your Twilio app couldn't "
                                             "be created: {0}".format(e))
            elif choice == "n" or i >= 3:
                raise ConfigurationError("Your APP_SID setting must be  "
                                         "set in local_settings.")
            else:
                logging.error("Please choose yes or no with a 'y' or 'n'")
        if app:
            logging.info("Application created: {0}".format(app.sid))
            self.app_sid = app.sid
            return app
        else:
            raise ConfigurationError("There was an unknown error "
                                     "creating your TwiML application.")

    def setAppRequestUrls(self, app_sid, voice_url, sms_url):
        logging.info("Setting request urls for application sid: "
                     "{0}".format(app_sid))

        try:
            app = self.client.applications.update(app_sid, voice_url=voice_url,
                                                  sms_url=sms_url,
                                                  friendly_name="Hackpack for "
                                                                "Heroku and "
                                                                "Flask")
        except TwilioException as e:
            if "HTTP ERROR 404" in str(e):
                raise ConfigurationError("This application sid was not "
                                         "found: {0}".format(app_sid))
            else:
                raise ConfigurationError("An error setting the request URLs "
                                         "occured: {0}".format(e))
        if app:
            logging.debug("Updated application sid: {0}".format(app.sid))
            return app
        else:
            raise ConfigurationError("An unknown error occuring "
                                     "configuring request URLs for app sid.")

    def retrievePhoneNumber(self, phone_number):
        logging.debug("Retrieving phone number: {0}".format(phone_number))
        try:
            logging.debug("Getting sid for phone number: "
                          "{0}".format(phone_number))
            number = self.client.phone_numbers.list(phone_number=phone_number)
        except TwilioException as e:
            raise ConfigurationError("An error setting the request URLs "
                                     "occured: {0}".format(e))
        if number:
            logging.debug("Retrieved sid: {0}".format(number[0].sid))
            self.friendly_phone_number = number[0].friendly_name
            return number[0]
        else:
            raise ConfigurationError("An unknown error occurred retrieving "
                                     "number: {0}".format(phone_number))

    def purchasePhoneNumber(self):
        logging.debug("Asking user to purchase phone number...")

        i = 0
        while True:
            i = i + 1
            # Find number to purchase
            choice = raw_input("Your CALLER_ID is not configured in your "
                               "local_settings.  Purchase a new one? "
                               "[y/n]").lower()
            if choice == "y":
                break
            elif choice == "n" or i >= 3:
                raise ConfigurationError("To configure this "
                                         "hackpack CALLER_ID must set in "
                                         "local_settings or a phone number "
                                         "must be purchased.")
            else:
                logging.error("Please choose yes or no with a 'y' or 'n'")

        logging.debug("Confirming purchase...")
        i = 0
        while True:
            i = i + 1
            # Confirm phone number purchase.
            choice = raw_input("Are you sure you want to purchase? "
                               "Your Twilio account will be charged $1. "
                               "[y/n]").lower()
            if choice == "y":
                try:
                    logging.debug("Purchasing phone number...")
                    number = self.client.phone_numbers.purchase(area_code="6"
                                                                          "46")
                    logging.debug("Phone number purchased: "
                                  "{0}".format(number.friendly_name))
                    break
                except TwilioException as e:
                    raise ConfigurationError("Your Twilio app couldn't "
                                             "be created: {0}".format(e))
            elif choice == "n" or i >= 3:
                raise ConfigurationError("To configure this hackpack "
                                         "CALLER_ID must set in "
                                         "local_settings or a phone number "
                                         "must be purchased.")
            else:
                logging.error("Please choose yes or no with a 'y' or 'n'")

        # Return number or error out.
        if number:
            logging.debug("Returning phone number: "
                          "{0}".format(number.friendly_name))
            self.phone_number = number.phone_number
            self.friendly_phone_number = number.friendly_name
            return number
        else:
            raise ConfigurationError("There was an unknown error purchasing "
                                     "your phone number.")

    def getHerokuHostname(self, git_config_path='./.git/config'):
        logging.debug("Getting hostname from git configuration file: "
                      "{0}".format(git_config_path))
        # Load git configuration
        try:
            logging.debug("Loading git config...")
            git_config = open(git_config_path).readlines()
        except IOError as e:
            raise ConfigurationError("Could not find .git config.  Does it "
                                     "still exist? Failed path: {0}".format(e))

        logging.debug("Finding Heroku remote in git configuration...")
        subdomain = None
        for line in git_config:
            if "git@heroku.com" in line:
                s = line.split(":")
                subdomain = s[1].replace('.git', '')
                logging.debug("Heroku remote found: {0}".format(subdomain))

        if subdomain:
            host = "http://{0}.herokuapp.com".format(subdomain.strip())
            logging.debug("Returning full host: {0}".format(host))
            return host
        else:
            raise ConfigurationError("Could not find Heroku remote in "
                                     "your .git config.  Have you "
                                     "created the Heroku app?")

    def printLocalEnvironmentVariableCommands(self, **kwargs):
        logging.info("Copy/paste these commands to set your local "
                     "environment to use this hackpack...")
        print("\n")
        for k, v in kwargs.items():
            if v:
                print("export {0}={1}\n".format(k, v))

    def setHerokuEnvironmentVariables(self, **kwargs):
        logging.info("Setting Heroku environment variables...")
        envvars = ["{0}={1}".format(k, v) for k, v in kwargs.items() if v]
        envvars.insert(0, "heroku")
        envvars.insert(1, "config:add")
        return subprocess.call(envvars)


class ConfigurationError(Exception):
    def __init__(self, message):
        #Exception.__init__(self, message)
        logging.error(message)


# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Parser configuration
parser = ArgumentParser(description="Twilio Hackpack Configurator - an "
                                    "easy way to configure your hackpack!",
                        epilog="Written by Rob Spectre.\n "
                               "http://www.brooklynhacker.com")
parser.add_argument("-S", "--account_sid", default=None,
                    help="Use a specific Twilio ACCOUNT_SID.")
parser.add_argument("-K", "--auth_token", default=None,
                    help="Use a specific Twilio AUTH_TOKEN.")
parser.add_argument("-n", "--new", default=False, action="store_true",
                    help="Purchase new Twilio phone number and configure "
                         "app to use your hackpack.")
parser.add_argument("-N", "--new_app", default=False, action="store_true",
                    help="Create a new TwiML application sid to use for your "
                         "hackpack.")
parser.add_argument("-a", "--app_sid", default=None,
                    help="Configure specific AppSid to use your hackpack.")
parser.add_argument("-#", "--phone-number", default=None,
                    help="Configure specific Twilio number to use your "
                         "hackpack.")
parser.add_argument("-v", "--voice_url", default=None,
                    help="Set the route for your Voice Request URL: "
                         "(e.g. '/voice').")
parser.add_argument("-s", "--sms_url", default=None,
                    help="Set the route for your SMS Request URL: "
                         "(e.g. '/sms').")
parser.add_argument("-d", "--domain", default=None,
                    help="Set a custom domain.")
parser.add_argument("-D", "--debug", default=False,
                    action="store_true", help="Turn on debug output.")


def main():
    # Configurator configuration :)
    configure = Configure()
    parser.parse_args(namespace=configure)

    # Options tree
    if configure.account_sid:
        configure.account_sid = configure.account_sid
    if configure.auth_token:
        configure.auth_token = configure.auth_token
    if configure.new:
        configure.phone_number = None
    if configure.new_app:
        configure.app_sid = None
    if configure.app_sid:
        configure.app_sid = configure.app_sid
    if configure.phone_number:
        configure.phone_number = configure.phone_number
    if configure.voice_url:
        configure.voice_url = configure.voice_url
    if configure.sms_url:
        configure.sms_url = configure.sms_url
    if configure.domain:
        configure.host = configure.domain
    if configure.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s - %(message)s')

    configure.start()

if __name__ == "__main__":
    main()
