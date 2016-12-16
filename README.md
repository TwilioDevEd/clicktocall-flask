<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Click to Call with Flask

This is an application example implementing Click to Call using Twilio.

[![Build Status](https://travis-ci.org/TwilioDevEd/clicktocall-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/clicktocall-flask)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/clicktocall-flask/badge.svg)](https://coveralls.io/r/TwilioDevEd/clicktocall-flask)

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/click-to-call/python/flask)!

## Installation

Step-by-step on how to deploy, configure and develop on this example app.

### Fastest Deploy

Use Heroku to deploy this app immediately:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/clicktocall-flask)

### Getting Started

1. Grab the latest source.

   ```bash
   $ git clone git://github.com/TwilioDevEd/clicktocall-flask.git
   ```

1. Navigate to folder and create new Heroku Cedar app.

   ```bash
   $ heroku create
   ```

1. Deploy to Heroku.

   ```bash
   $ git push heroku master
   ```

1. Scale your dynos.

   ```bash
   $ heroku scale web=1
   ```

1. Visit the home page of your new Heroku app to see your newly configured app!

   ```bash
   $ heroku open
   ```

### Configuration

Want to use the built-in Twilio Client template?  Configure your app with
three easy options.

#### Automatic Configuration

This app ships with an auto-configure script that will create a new TwiML
app. Purchase a new phone number and set your Heroku app's environment
variables to be used with your new settings.  Here's a quick step-by-step:

1. Make sure you have all dependencies installed.

   ```bash
   $ make init
   ```

1. Run configure script and follow instructions.

   ```bash
   $ python configure.py --account_sid ACxxxxxx --auth_token yyyyyyy
   ```

1. For local development, copy/paste the environment variable commands the configurator provides to your shell.

   ```bash
   export TWILIO_ACCOUNT_SID=ACxxxxxx
   export TWILIO_AUTH_TOKEN=yyyyyyyyy
   export TWILIO_APP_SID=APzzzzzzzzzz
   export TWILIO_PHONE=+15556667777
   ```

Automagic configuration comes with a number of features.  
`python configure.py --help` to see them all.

#### `local_settings.py`

`local_settings.py` is a file available on the app route for you to configure
your twilio account credentials manually.  Be sure not to expose your Twilio
account to a public repo though.

```python
ACCOUNT_SID = "ACxxxxxxxxxxxxx"
AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_APP_SID = "APzzzzzzzzz"
TWILIO_PHONE = "+17778889999"
```

#### Setting Your Own Environment Variables

The application configurator will automatically use your environment variables. You
can set your own TwiML app and phone number if you prefer to.  The environment
variables are required to configure and run the Twilio and Heroku apps.

1. Set environment variables locally.

   ```bash
   export TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxx
   export TWILIO_AUTH_TOKEN=yyyyyyyyyyyyyyyyy
   export TWILIO_APP_SID=APzzzzzzzzzzzzzzzzzz
   export TWILIO_PHONE=+15556667777
   ```

1. Run configurator.

   ```bash
   $ python configure.py
   ```

### Development

Getting your local environment setup to work with this app is easy.
After you configure your app with the steps above use this guide to
get it going locally.

1. Install the dependencies.

   ```bash
   $ make init
   ```

1. Launch local development webserver.

   ```bash
   $ foreman start
   ```

1. Open browser to [http://localhost:5000](http://localhost:5000).

1. Tweak away on `clicktocall/app.py`.

## Testing

This app comes with a full testing suite ready for nose.

```bash
$ make test
```

It also ships with an easy-to-use base class for testing your
[TwiML](http://www.twilio.com/docs/api/twiml).  For example, testing a basic SMS
response is only two lines of code.

```python
import test_twilio

class ExampleTest(test_twilio.TwiMLTest):
    response = self.sms("Test")
    self.assertTwiML(response)
```

You can also test your [Gather
verbs](http://www.twilio.com/docs/api/twiml/gather) for voice apps very easily.

```python
import test_twilio

class ExampleTest(test_twilio.TwiMLTest):
    response = self.call(digits="1")
    self.assertTwiML(response)
```

## Meta

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
