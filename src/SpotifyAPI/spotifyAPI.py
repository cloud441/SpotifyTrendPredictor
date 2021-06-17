import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint


class APIManager:

    def __init__(self, user='spotify_client'):
        self.user = user

        if (user == 'spotify_client'):
            token = SpotifyClientCredentials(client_id='c8464bcbd6ba4e5f97b3c7e0f5a5a3be',
                    client_secret='91cfce9387b0463ab0e5ef2043d0a9c9')

            if token:
                self.api = spotipy.Spotify(client_credentials_manager=token)
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
        if (self.user != 'spotify_client'):
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


    def get_trends_playlist(self, nb_entries):
        if (self.user != 'spotify_client'):
            print(f'Error: Impossible to load spotify playlist  with user {self.user}')
            return


        top_50_global_id = 'spotify:playlist:37i9dQZEVXbNG2KDcFcKOF'
        response = self.api.playlist_items(top_50_global_id,
                fields='items.track.id,total',
                additional_types=['track'])

        if (response['total'] != 0):
            return [self.api.track("spotify:track:" + track['track']['id']) for track in response['items']]

        return []
