<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Click to Call with Flask

> This repository is archived and no longer maintained. Check out the [Twilio Voice](https://www.twilio.com/docs/voice/) docs for links to other tutorials. 

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
   [here](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html) for more details. This step
   is important because the application won't work as expected if you run it through
   localhost.

   ```bash
   ngrok http 5000
   ```

6. Once Ngrok is running, open up your browser and go to your Ngrok URL. It will
look like this: `http://9a159ccf.ngrok.io`

That's it!

### Docker

If you have [Docker](https://www.docker.com/) already installed on your machine, you can use our `docker-compose.yml` to setup your project.

1. Make sure you have the project cloned.
2. Setup the `.env` file as outlined in the [Local Development](#local-development) steps.
3. Run `docker-compose up`.
4. Follow the steps in [Local Development](#local-development) on how to expose your port to Twilio using a tool like [ngrok](https://ngrok.com/) and configure the remaining parts of your application.


### Tests

To execute tests, run the following command in the project directory. Before running the following command, make sure the virtual environment is activated.

```bash
make test
```

## Resources

- The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
