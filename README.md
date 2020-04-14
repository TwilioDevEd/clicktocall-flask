<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Click to Call with Flask

This is an application example implementing Click to Call using Twilio.

![](https://github.com/TwilioDevEd/clicktocall-flask/workflows/Flask/badge.svg)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/clicktocall-flask/badge.svg)](https://coveralls.io/r/TwilioDevEd/clicktocall-flask)

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/click-to-call/python/flask)!

## Local development

This project is built using the [Flask](https://flask.palletsprojects.com/) web framework. It runs on Python 2.7+ and Python 3.4+.

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
* The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
