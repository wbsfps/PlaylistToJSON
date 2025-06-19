from dotenv import load_dotenv
import os
load_dotenv()

from functions.spotify import get_token, get_playlist

CLIENT_ID = os.getenv("CLIENT_ID_SPOTIFY")
SECRET_ID = os.getenv("CLIENT_SECRET_SPOTIFY")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")
url = os.getenv("GET_TOKEN_URL_SPOTIFY")

token = get_token.get_token(url, client_id=CLIENT_ID, secret_id=SECRET_ID)

playlist = get_playlist.get_playlist(playlist_id=PLAYLIST_ID, token=token)

print(token)
print(playlist)