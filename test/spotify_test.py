
import os
from unicodedata import name
import pytest
import spotipy
import spotipy.oauth2
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from app.spotify_service import artist_recommendation
#SET VARIABLES WITH ENV INFO
CLIENT_ID = os.environ.get("CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "OOPS")

#SET UP CODE SO WE CAN USE THE SPOTIPY API DATA
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_reccommendations():
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
    #with valid name, returns the reccommended artists and songs:
    results = artist_recommendation(name = "Dua Lipa")
    assert artist['name']
    
    #with invalid name, fails gracefully and returns nothing:
    invalid_results = artist_recommendation(name=129112)
    assert invalid_results == None

