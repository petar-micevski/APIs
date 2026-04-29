import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8080'

def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-read-private user-read-email'
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def get_user_info(sp):
    try:
        user = sp.current_user()
        print("Spotify User Info:")
        print(f"Display Name: {user['display_name']}")
        print(f"Email: {user['email']}")
        print(f"Country: {user['country']}")
        return user
    except Exception as e:
        print(f"Error getting Spotify user info: {e}")
        return None

def search_track(sp, query):
    try:
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            print(f"Spotify Track: {track['name']} by {track['artists'][0]['name']}")
            return track
        else:
            print("No tracks found on Spotify")
            return None
    except Exception as e:
        print(f"Error searching Spotify: {e}")
        return None