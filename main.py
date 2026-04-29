from spotify_api import get_spotify_client, get_user_info, search_track as spotify_search
from soundcloud_api import search_track as soundcloud_search
from scraper import scrape_multiple

def main():
    print("Connecting to APIs...\n")

    # Spotify
    print("=== Spotify API ===")
    sp = get_spotify_client()
    if sp:
        get_user_info(sp)
        print()
        spotify_search(sp, 'hello')
    else:
        print("Failed to connect to Spotify")

    print("\n=== SoundCloud API ===")
    soundcloud_search('hello')

    print("\n=== Web Scraper ===")
    # List of URLs to scrape - replace with actual chord website URLs
    urls = [
        # 'https://tabs.ultimate-guitar.com/tab/artist/song-chords-123456',
        # Add your URLs here
    ]
    if urls:
        scraped_data = scrape_multiple(urls)
        for i, data in enumerate(scraped_data):
            print(f"\nSong {i+1}:")
            if 'error' in data:
                print(f"Error: {data['error']}")
            else:
                print(f"Song Name: {data['song_name']}")
                print(f"Artist: {data['artist']}")
                print(f"Key: {data['key']}")
                print(f"Chords until first chorus:\n{data['chords']}")
    else:
        print("No URLs provided for scraping. Add URLs to the 'urls' list in main.py")

if __name__ == "__main__":
    main()