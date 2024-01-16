import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import client
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
    scope="playlist-modify-private",
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]

# GET TOP 100 SONG NAME LIST
year_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{year_input}/"

response = requests.get(url)
bb_web = response.text

soup = BeautifulSoup(bb_web, "html.parser")
all_song = soup.select(selector="li .o-chart-results-list__item #title-of-a-story")
song_list = [song.getText().strip() for song in all_song]

# SEARCH FOR SONG URI
uri_list = []
for name in song_list:
    try:
        result = sp.search(q=name, limit=1, type="track")['tracks']["items"][0]
    except IndexError:
        pass
    else:
        uri_list.append(result["uri"])

playlist = sp.user_playlist_create(user=user_id, name=f"{year_input} Billboard 100", public=False)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=uri_list)
