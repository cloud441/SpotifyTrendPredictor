import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint



PLAYLIST_TOP_50_GLOBAL = 'spotify:playlist:37i9dQZEVXbNG2KDcFcKOF'
PLAYLIST_FORGOTIFY = 'spotify:playlist:4ItpnreD2Bkmu3D9OKEQip'


class APIManager:

    def __init__(self, user='spotify_client'):
        self.user = user

        # Connect with Spotify global client:
        if (user == 'spotify_client'):
            # Create Spotify client:
            token = SpotifyClientCredentials(client_id='c8464bcbd6ba4e5f97b3c7e0f5a5a3be',
                    client_secret='91cfce9387b0463ab0e5ef2043d0a9c9')

            # Load Spotify api interface:
            if token:
                self.api = spotipy.Spotify(client_credentials_manager=token)
            else:
                print("Can't get token for", username)

        # Connect with Specific user credentials:
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


    def get_tracks_audio_features(self, track_ids):
        response = []

        for i in range(round(len(track_ids) / 100)):
            upper_bound = min(len(track_ids), (i + 1) * 100)
            response += self.api.audio_features(track_ids[i * 100:upper_bound])


        return response




    def get_playlist(self, playlist_id):
        if (self.user != 'spotify_client'):
            print(f'Error: Impossible to load spotify playlist  with user {self.user}')
            return


        # Request all playlist tracks:
        response = self.api.playlist_items(playlist_id,
                fields='items.track.id,total',
                additional_types=['track'])

        if (response['total'] != 0):
            # Request tracks metadata:
            return [self.api.track("spotify:track:" + track['track']['id']) for track in response['items']]

        return []



    def get_trends_playlist(self):
        return self.get_playlist(PLAYLIST_TOP_50_GLOBAL)


    def get_forgotify_playlist(self):
        return self.get_playlist(PLAYLIST_FORGOTIFY)
