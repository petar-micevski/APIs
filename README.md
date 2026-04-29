# API Connections and Web Scraping Project

This project demonstrates how to connect to Spotify and SoundCloud APIs using Python, and includes a web scraper for extracting song information from chord websites.

## Prerequisites

- Python 3.8 or higher
- Spotify Developer Account
- SoundCloud Developer Account

## Setup

1. Clone or download this project.

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Get API credentials:

   ### Spotify
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Copy the Client ID and Client Secret
   - Add `http://localhost:8080` as a redirect URI

   ### SoundCloud
   - Go to [SoundCloud Developer](https://developers.soundcloud.com/)
   - Create a new app
   - Copy the Client ID and Client Secret

4. Create a `.env` file in the root directory with your credentials:
   ```
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SOUNDCLOUD_CLIENT_ID=your_soundcloud_client_id
   SOUNDCLOUD_CLIENT_SECRET=your_soundcloud_client_secret
   ```

## Usage

Run the main script:
```
python main.py
```

This will authenticate with both APIs and fetch some basic information.

## Files

- `main.py`: Main script to run the API connections and web scraping
- `spotify_api.py`: Spotify API connection and functions
- `soundcloud_api.py`: SoundCloud API connection and functions
- `scraper.py`: Web scraping functions using BeautifulSoup
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (not committed)

## Web Scraper

The project includes a web scraper using BeautifulSoup to extract song information from chord websites.

- Extracts song name, artist, key, and chords until the end of the first chorus
- Takes a list of URLs as input
- Example usage in `main.py`

**Note**: Web scraping should comply with the website's terms of service. The scraper is designed for educational purposes and may need adjustments for specific website structures.