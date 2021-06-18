import pandas as pd


class DataLogger:

    def __init__(self):
        self.df = pd.DataFrame()


    def load_trend_dataset(self, api_manager):
        # Merge two playlists for first test:
        merged_playlists = api_manager.get_trends_playlist() + api_manager.get_forgotify_playlist()
        self.df = pd.json_normalize(merged_playlists, max_level=2)

        print(f'\nBasic data columns are:\n\n{self.df.columns}')

        # Add audio features info to tracks:
        self.df.drop(columns=['duration_ms', 'uri'], inplace=True)
        audio_feature_df = pd.json_normalize(api_manager.get_tracks_audio_features(self.df['id'].to_list()), max_level=2)
        print(f'\nAudio features columns are:\n\n{audio_feature_df.columns}')

        self.df = self.df.merge(audio_feature_df, on='id', how='inner')

        return self.df


    # Do some pre-processing (filtering, simplify data, etc ...)
    def apply_pre_processing(self):
        self.df['artists'] = self.df['artists'].map(lambda artists : artists[0]['name'])
        self.df.rename(columns={'artists' : 'artist'}, inplace=True)

        self.df.drop(columns=['disc_number', 'available_markets', 'href', 'preview_url', 'uri', 'album.artists', 'album.available_markets',
                    'album.external_urls.spotify', 'album.href', 'album.id', 'album.images', 'album.uri',
                    'external_ids.isrc', 'external_urls.spotify', 'id', 'track_href', 'analysis_url'], inplace=True)

        return self.df



    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False)
