import os
from unicodedata import name

from matplotlib import artist
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

#function searches by artist name and returns the artist ID
def search_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        global artist_id 
        artist_id = artist['id']
        return(artist_id)
    else:
        print("There are no results for your input.")
        quit()

#tested search function
#search_artist(name)

print(artist_id)

similar_artists = []

def get_similar_artists(artist_id):
    related_artists = sp.artist_related_artists(artist_id)
    for n in related_artists['artists']:
        similar_artists.append(n['name'])
    return(similar_artists[0:5])

get_similar_artists(artist_id)




