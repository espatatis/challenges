import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'sz08l1r9jm94jvyaeohhp9gjm'
token = util.prompt_for_user_token(username, scope, client_id='6b1358d2a8f54d6b86356e66d4b5c144', client_secret='06713d07f16643b0ad1c5cafe7b9a09e', redirect_uri='http://google.com/')

if token:
    artist_name = input('The artist URI : ')
    sp = spotipy.Spotify(auth=token)
    results = sp.artist_albums(artist_name, album_type = 'album')
    albums = results['items']
    try:
        while results['items']:
            results = sp.next(results)
            try:
                albums.extend(results['items'])
            except TypeError:
                pass
    except TypeError:
            pass

    for album in albums:
        print(album['name'])
else:
    pass
