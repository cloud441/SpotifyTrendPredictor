import spotipy
import spotipy.util as util


class APIManager:

    def __init__(self):
        self.user = 'cloud_441'
        token = util.prompt_for_user_token(self.user,
                'user-library-read',
                client_id='c8464bcbd6ba4e5f97b3c7e0f5a5a3be',
                client_secret='91cfce9387b0463ab0e5ef2043d0a9c9',
                redirect_uri='http://localhost/')
        print("Authorization configuration is done.")

        if token:
            self.api = spotipy.Spotify(auth=token)
        else:
            print("Can't get token for", username)
