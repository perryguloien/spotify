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

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:
# required vars:
CLIENT_ID = "______________"
CLIENT_SECRET = "______________"

## Usage

```sh
python -m app.spotify_service

## Testing

Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server.

## [License](/LICENSE.md)

Running python on server: 

```sh
FLASK_APP=web_app flask run

flask run

