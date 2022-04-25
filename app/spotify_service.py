import os
from unicodedata import name
from dotenv import load_dotenv
import sys

import spotipy
import spotipy.oauth2
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv() # load environment variables 
#ENV VARIABLES
CLIENT_ID = os.environ.get("CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "OOPS")
#INPUT VARIABLE
name = input("Artist Full Name:")


#SET UP CODE SO WE CAN USE THE SPOTIPY API DATA
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


results = sp.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    artist_id = (artist['id'])

    if artist_id is None:
        print("There are no results for your input.")
        exit()

similar_artists = []

related_artists = sp.artist_related_artists(artist_id)
for n in related_artists['artists']:
    similar_artists.append(n['name'])
print(similar_artists[0:5])





