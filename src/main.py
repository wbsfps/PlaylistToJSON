from dotenv import load_dotenv
import os
load_dotenv()

from services.spotify_api.get_token import get_token
from services.spotify_api.get_playlist import get_playlist
from services.spotify_api.get_musics_of_playlist import get_musics_of_playlist

from src.utils.send_data_to_json import send_data_to_json

CLIENT_ID = os.getenv("CLIENT_ID_SPOTIFY")
SECRET_ID = os.getenv("CLIENT_SECRET_SPOTIFY")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")
url = os.getenv("GET_TOKEN_URL_SPOTIFY")

token = get_token(url, client_id=CLIENT_ID, secret_id=SECRET_ID)

playlist = get_playlist(playlist_id=PLAYLIST_ID, token=token)

musics = get_musics_of_playlist(playlist)

send_data_to_json(musics, "src/assets/musics/musics.json")