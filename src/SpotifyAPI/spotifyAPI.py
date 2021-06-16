import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


class APIManager:

    def __init__(self, user='spotify_oauth'):
        self.user = user

        if (user == 'spotify_oauth'):
            token = SpotifyOAuth(client_id='c8464bcbd6ba4e5f97b3c7e0f5a5a3be',
                    client_secret='91cfce9387b0463ab0e5ef2043d0a9c9',
                    redirect_uri='http://localhost/')

            if token:
                self.api = spotipy.Spotify(auth_manager=token)
            else:
                print("Can't get token for", username)

        else:
            token = util.prompt_for_user_token(self.user,
                    'user-library-read',
                    client_id='c8464bcbd6ba4e5f97b3c7e0f5a5a3be',
                    client_secret='91cfce9387b0463ab0e5ef2043d0a9c9',
                    redirect_uri='http://localhost/')

            if token:
                self.api = spotipy.Spotify(auth=token)
            else:
                print("Can't get token for", username)


    def get_new_released(self):
        if not (self.user == 'spotify_oauth'):
            print(f'Error: Impossible to load new release song with user {self.user}')
            return

        response = self.api.new_releases()

        while response:
            albums = response['albums']
            for i, item in enumerate(albums['items']):
                print(albums['offset'] + i, item['name'])

                if albums['next']:
                    response = self.api.next(albums)
                else:
                    response = None

