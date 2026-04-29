import requests
from bs4 import BeautifulSoup

def scrape_song_info(url):
    """
    Scrape song information from a chord/lyrics website.
    Assumes the site has:
    - Title in <title> tag (format: "Song Name Chords - Artist")
    - Key mentioned in <p> tags as "Key: ..."
    - Chords in <pre> or <div class="tab"> or <div class="js-tab-content">
    - Extracts chords until the end of the first [Chorus] section if found.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract song name and artist from <title>
        title_tag = soup.find('title')
        if title_tag:
            full_title = title_tag.text.strip()
            if ' - ' in full_title:
                song_name, artist = full_title.split(' - ', 1)
                song_name = song_name.replace(' Chords', '').replace(' Tabs', '').strip()
                artist = artist.strip()
            else:
                song_name = full_title
                artist = 'Unknown'
        else:
            song_name = 'Unknown'
            artist = 'Unknown'

        # Extract key from page text
        key = 'Unknown'
        for element in soup.find_all(['p', 'div', 'span']):
            text = element.get_text()
            if 'Key:' in text:
                key = text.split('Key:')[1].strip().split()[0]  # Take first word
                break

        # Extract chords
        chords_element = (soup.find('pre') or
                         soup.find('div', class_='tab') or
                         soup.find('div', class_='js-tab-content') or
                         soup.find('div', {'data-content': True}))
        if chords_element:
            chords_text = chords_element.get_text(separator='\n')
            # Find the first [Chorus] and take up to its end
            chorus_start = chords_text.find('[Chorus]')
            if chorus_start != -1:
                # Find the end of the chorus section (next section or end)
                next_section = chords_text.find('[', chorus_start + 1)
                if next_section != -1:
                    chords = chords_text[:next_section].strip()
                else:
                    chords = chords_text[:chorus_start + len('[Chorus]')].strip()
            else:
                chords = chords_text.strip()
        else:
            chords = 'Chords not found'

        return {
            'song_name': song_name,
            'artist': artist,
            'key': key,
            'chords': chords
        }
    except Exception as e:
        return {'error': str(e)}

def scrape_multiple(urls):
    """
    Scrape information from a list of URLs.
    """
    results = []
    for url in urls:
        print(f"Scraping {url}...")
        info = scrape_song_info(url)
        results.append(info)
    return results