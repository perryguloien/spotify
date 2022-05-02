import os

from dotenv import load_dotenv
import sys

import spotipy
import spotipy.oauth2
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv() # load environment variables 

#SET VARIABLES WITH ENV INFO
#CLIENT_ID = os.environ.get("CLIENT_ID", "OOPS")
CLIENT_ID = "c022c9885abd4227be5dcae0b09ff1bb"
CLIENT_SECRET = "aa32b3abaceb4f38b77fc36571db840b"
#CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "OOPS")

#SET UP CODE SO WE CAN USE THE SPOTIPY API DATA
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#function searches by artist name and returns the artist reccommendations and reccomended songs
def artist_recommendation(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0] 
        artist_id = artist['id']
        similar_artists = []
        similar_artists_ids = []
        related_artists = sp.artist_related_artists(artist_id)

        for n in related_artists['artists'][0:5]:
            similar_artists.append({"names": n['name'], "display_images": n['images'][1]['url'], "songs": [] })
            similar_artists_ids.append(n['id'])
        
        name_res = artist['name']
        
        b = 0
        for artist in similar_artists:
            _id = similar_artists_ids[b]
            related_songs = sp.artist_top_tracks(_id)
            a = 0
            hold_songs = []
            while a < 5:
                hold = related_songs['tracks'][a]['name'] 
                hold_songs.append(hold)
                a = a + 1 
            artist['songs'] = hold_songs
            b = b+1
        print("------------------------------------------")
        print(similar_artists[0:5])
        return(similar_artists[0:5], name_res)
  
    else:
        print("There are no results for your input.")
        return None

if __name__ == "__main__":
    #INPUT VARIABLE
    name = input("Artist Full Name:")
    artist_recommendation(name)
