import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('SOUNDCLOUD_CLIENT_ID')
CLIENT_SECRET = os.getenv('SOUNDCLOUD_CLIENT_SECRET')

def search_track(query):
    try:
        url = f'https://api.soundcloud.com/tracks?client_id={CLIENT_ID}&q={query}&limit=1'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                track = data[0]
                print("SoundCloud Track:")
                print(f"Title: {track['title']}")
                print(f"Artist: {track['user']['username']}")
                print(f"Duration: {track['duration'] // 1000} seconds")
                return track
            else:
                print("No tracks found on SoundCloud")
                return None
        else:
            print(f"SoundCloud API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error searching SoundCloud: {e}")
        return None

# Note: For full user authentication, SoundCloud requires OAuth flow, which is more complex.
# This example uses the public API for searching tracks.