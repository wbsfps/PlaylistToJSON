import requests as rq
import os

GET_ONE_PLAYLIST_SPOTIFY = os.getenv("GET_ONE_PLAYLIST_SPOTIFY")

def get_playlist(playlist_id, token) -> None:
    url = f'{GET_ONE_PLAYLIST_SPOTIFY}{playlist_id}'

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = rq.get(url, headers=headers)

    if response.status_code == 200:
        playlist = response.json()
        return playlist
    else:
        return (response.status_code, response.text)