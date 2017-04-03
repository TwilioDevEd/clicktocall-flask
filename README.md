<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Click to Call with Flask

This is an application example implementing Click to Call using Twilio.

[![Build Status](https://travis-ci.org/TwilioDevEd/clicktocall-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/clicktocall-flask)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/clicktocall-flask/badge.svg)](https://coveralls.io/r/TwilioDevEd/clicktocall-flask)

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/click-to-call/python/flask)!

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv clicktocall-flask
        ```

1. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

1. Copy the `.env.example` file to `.env`, and edit it including your credentials
   for the Twilio API (found at https://www.twilio.com/user/account/settings). You
   will also need a [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming).
1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Expose your application to the wider internet using ngrok. You can click
   [here](#expose-the-application-to-the-wider-internet) for more details. This step
   is important because the application won't work as expected if you run it through
   localhost.

   ```bash
   $ ngrok http 5000
   ```

1. Start the development server:

    ```
    make run
    ```

Once Ngrok is running, open up your browser and go to your Ngrok URL. It will
look like this: `http://9a159ccf.ngrok.io`

That's it!

## Testing

This app comes with a full testing suite ready for nose.

```bash
$ make test
```

## Meta

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
