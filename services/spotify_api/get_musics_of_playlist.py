def get_musics_of_playlist(playlist: dict):
    musics = []

    tracks = playlist.get("tracks")
    if not tracks:
        return musics

    items = tracks.get("items")
    if not items:
        return musics

    for item in items:
        track = item.get("track")
        if track:
            musics.append(track.get("name", "Sem nome"))

    return musics