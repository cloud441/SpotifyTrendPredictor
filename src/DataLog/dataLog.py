import pandas as pd


class DataLogger:

    def __init__(self):
        self.df = pd.DataFrame()


    def load_trend_dataset(self, api_manager, nb_entries=500):

        # need to fix loading to manage JSON format:
        self.df = pd.DataFrame(api_manager.get_trends_playlist(nb_entries))
        return self.df


    def save_to_csv(self, filename):
        self.df.to_csv(filename, index=False)
