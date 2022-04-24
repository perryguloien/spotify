# Spotify Artist Recommendation App (Python)

Sends you a customized email with artist recommendations based on previously liked artists linked to a user's Spotify account. 

## Installation

Create a copy of this repo (https://github.com/perryguloien/spotify), then clone or download your new repo onto your local computer (for example to the Desktop), and navigate there from the command-line:

```sh
cd ~/Desktop/spotify/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "spotify-env":

```sh
conda create -n spotify-env python=3.8
conda activate spotify-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API key (i.e. `SENDGRID_API_KEY`).


Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"

# optional vars: 

## Usage

Printing today's weather forecast (to test the Weather.gov API):

```sh
python -m app.weather_service

# in production mode:
APP_ENV="production" COUNTRY_CODE="US" ZIP_CODE="20057" python -m app.weather_service
```

Sending an example email (to test the SendGrid service):

```sh
python -m app.email_service
```

> NOTE: the SendGrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")

Sending the weather forecast in an email:

```sh
python -m app.daily_briefing

# in production mode:
APP_ENV="production" COUNTRY_CODE="US" ZIP_CODE="20057" python -m app.daily_briefing
```


## Testing

Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```


## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server and schedule the server to send you the weather forecast email every day.

## [License](/LICENSE.md)

Running python on server: 


```sh
FLASK_APP=web_app flask run

flask run

## TEST