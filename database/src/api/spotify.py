import json
import pandas as pd
import matplotlib.pyplot as plt

with open('spotify_library\YourLibrary.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

df = pd.DataFrame(data['tracks'])

df['artist'].value_counts().head(30).plot(kind='bar', title='Top 30 Artists in Your Spotify Library')