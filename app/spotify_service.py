import os

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

#SET UP CODE SO WE CAN USE THE SPOTIPY API DATA
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#function searches by artist name and returns the artist ID
def artist_recommendation(name):
    #search from the spotipy api
    results = sp.search(q='artist:' + name, type='artist')
    #results = sp.search(name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0] 
        artist_id = artist['id']
        similar_artists = []
        related_artists = sp.artist_related_artists(artist_id)
        for n in related_artists['artists']:
            similar_artists.append(n['name'])
        print(similar_artists[0:5])
        return(similar_artists[0:5])
    else:
        print("There are no results for your input.")
        return None

if __name__ == "__main__":
    #INPUT VARIABLE
    name = input("Artist Full Name:")
    artist_recommendation(name)




