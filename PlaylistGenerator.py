import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from pprint import pprint


date = input("What day do you want to go to? (YYYY-MM-DD): ")
year = date.split("-")[0]

link = f"https://www.billboard.com/charts/hot-100/2011-07-02/"

response = requests.get(link)
data = response.text

soup = BeautifulSoup(data, "html.parser")
titles = soup.select(".o-chart-results-list__item .c-title")
title_list = [title.getText()[14:-5] for title in titles]
song_uris = []

client_id = CLIENT_ID
client_secret = CLIENT_SECRET

auth_manager = SpotifyOAuth(client_id=client_id,
                                        client_secret=client_secret,
                                        scope="playlist-modify-private",
                                        redirect_uri="http://example.com",
                                        show_dialog=True,
                                        cache_path="token.txt"
                                        )
sp = spotipy.Spotify(auth_manager=auth_manager)

for title in title_list:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} is not on Spotify.")

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"Popular songs from {date}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
