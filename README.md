# Click to Call with Flask

This is an application example implementing Click to Call using Twilio.

[![Build Status](https://travis-ci.org/TwilioDevEd/clicktocall-flask.svg?branch=master)]
(https://travis-ci.org/TwilioDevEd/clicktocall-flask)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/clicktocall-flask/badge.png)]
(https://coveralls.io/r/TwilioDevEd/clicktocall-flask)

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/click-to-call/python/flask)!

## Installation

Step-by-step on how to deploy, configure and develop on this example app.

### Fastest Deploy

Use Heroku to deploy this app immediately:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/clicktocall-flask)

### Getting Started

1) Grab the latest source
```
$ git clone git://github.com/TwilioDevEd/clicktocall-flask.git
```

2) Navigate to folder and create new Heroku Cedar app
```
$ heroku create
```

3) Deploy to Heroku
```
$ git push heroku master
```

4) Scale your dynos
```
$ heroku scale web=1
```

5) Visit the home page of your new Heroku app to see your newly configured app!
```
$ heroku open
```


### Configuration

Want to use the built-in Twilio Client template?  Configure your app with
three easy options.

#### Automatic Configuration

This app ships with an auto-configure script that will create a new TwiML
app. Purchase a new phone number and set your Heroku app's environment
variables to be used with your new settings.  Here's a quick step-by-step:

1) Make sure you have all dependencies installed
```bash
$ make init
```

2) Run configure script and follow instructions
```
$ python configure.py --account_sid ACxxxxxx --auth_token yyyyyyy
```

3) For local development, copy/paste the environment variable commands the
configurator provides to your shell
```bash
export TWILIO_ACCOUNT_SID=ACxxxxxx
export TWILIO_AUTH_TOKEN=yyyyyyyyy
export TWILIO_APP_SID=APzzzzzzzzzz
export TWILIO_CALLER_ID=+15556667777
```

Automagic configuration comes with a number of features.  
`python configure.py --help` to see them all.


#### local_settings.py

local_settings.py is a file available on the app route for you to configure
your twilio account credentials manually.  Be sure not to expose your Twilio
account to a public repo though.

```python
ACCOUNT_SID = "ACxxxxxxxxxxxxx"
AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_APP_SID = "APzzzzzzzzz"
TWILIO_CALLER_ID = "+17778889999"
```

#### Setting Your Own Environment Variables

The application configurator will automatically use your environment variables. You
can set your own TwiML app and phone number if you prefer to.  The environment
variables are required to configure and run the Twilio and Heroku apps.

1) Set environment variables locally.

```
export TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxx
export TWILIO_AUTH_TOKEN=yyyyyyyyyyyyyyyyy
export TWILIO_APP_SID=APzzzzzzzzzzzzzzzzzz
export TWILIO_CALLER_ID=+15556667777
```

2) Run configurator
```
$ python configure.py
```


### Development

Getting your local environment setup to work with this app is easy.
After you configure your app with the steps above use this guide to
get it going locally.

1) Install the dependencies
```
$ make init
```

2) Launch local development webserver
```
$ foreman start
```

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `clicktocall/app.py`


## Testing

This app comes with a full testing suite ready for nose.

```
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


[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/33a5ddd61dd29dd933422bca2b3dfa0e
"githalytics.com")](http://githalytics.com/TwilioDevEd/clicktocall-flask)
