import pandas as pd


class DataLogger:

    def __init__(self):
        self.df = pd.DataFrame()


    def load_trend_dataset(self, api_manager):
        merged_playlists = api_manager.get_trends_playlist() + api_manager.get_forgotify_playlist()
        self.df = pd.json_normalize(merged_playlists, max_level=2)
        return self.df


    def apply_pre_processing(self):
        self.df['artists'] = self.df['artists'].map(lambda artists : artists[0]['name'])
        self.df.rename(columns={'artists' : 'artist'}, inplace=True)

        self.df.drop(columns=['disc_number', 'available_markets', 'href', 'preview_url', 'uri', 'album.artists', 'album.available_markets',
                    'album.external_urls.spotify', 'album.href', 'album.id', 'album.images', 'album.uri',
                    'external_ids.isrc', 'external_urls.spotify'], inplace=True)

        return self.df



    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False)
