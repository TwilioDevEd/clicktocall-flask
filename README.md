<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Click to Call with Flask

[![Build Status](https://travis-ci.org/TwilioDevEd/clicktocall-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/clicktocall-flask)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/clicktocall-flask/badge.svg)](https://coveralls.io/r/TwilioDevEd/clicktocall-flask)

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

## About

This is an application example implementing Click to Call using Twilio and [Flask](http://flask.pocoo.org/) web framework.

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/click-to-call/python/flask)!

Implementations in other languages:

| .NET | Java | Node | Ruby | PHP |
| :--- | :--- | :----- | :-- | :--- |
| [Done](https://github.com/TwilioDevEd/clicktocall-csharp)  | [Done](https://github.com/TwilioDevEd/clicktocall-spring)  | [Done](https://github.com/TwilioDevEd/clicktocall-node)  | [Done](https://github.com/TwilioDevEd/clicktocall-rails) | [Done](https://github.com/TwilioDevEd/clicktocall-php)  |


## Set up

### Requirements

- [Python](https://www.python.org/) **3.6**, **3.7** or **3.8** version.

In some environments when both version 2
and 3 are installed, you may substitute the Python executables below with
`python3` and `pip3` unless you use a version manager such as
[pyenv](https://github.com/pyenv/pyenv).

### Twilio Account Settings

This application should give you a ready-made starting point for writing your own application.
Before we begin, we need to collect all the config values we need to run the application:

| Config Value | Description                                                                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TWILIO_ACCOUNT_SID  | Your primary Twilio account identifier - find this [in the Console](https://www.twilio.com/console/project/settings).|
| TWILIO_AUTH_TOKEN   | Used to authenticate - just like the above, you'll find this [here](https://www.twilio.com/console/project/settings).|
| TWILIO_CALLER_ID | A Twilio phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://www.twilio.com/console/phone-numbers/incoming) |

### Local development

1. First clone this repository and `cd` into it.

   ```bash
   git clone https://github.com/TwilioDevEd/clicktocall-flask.git
   cd clicktocall-flask
   ```

2. Create the virtual environment, load it and install the dependencies.

    ```bash
    make install
    ```

3. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   cp .env.example .env
   ```

   See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

4. Start the development server, it will run on port 5000. Before running the following command, make sure the virtual environment is activated.

   ```bash
   make serve
   ```

5. Expose your application to the wider internet using ngrok. You can click
   [here](#expose-the-application-to-the-wider-internet) for more details. This step
   is important because the application won't work as expected if you run it through
   localhost.

   ```bash
   ngrok http 5000
   ```

6. Once Ngrok is running, open up your browser and go to your Ngrok URL. It will
look like this: `http://9a159ccf.ngrok.io`

That's it!

### Tests

To execute tests, run the following command in the project directory. Before running the following command, make sure the virtual environment is activated.

```bash
make test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                                                                           |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                                                                                                                       |

## Resources

- The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).

## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
