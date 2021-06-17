#!/usr/bin/env python

import sys
import SpotifyAPI
import DataLog


def run(argv):

    api_manager = SpotifyAPI.APIManager() if (len(argv[1:]) == 0) else SpotifyAPI.APIManager(user=argv[1])
    if not api_manager.api:
        print(f'Error: Impossible to established API connection with user {api_manager.user}')
        return

    print(f'\nThe API connection is established with user {api_manager.user}.\n')
    data_logger = DataLog.DataLogger()
    data_logger.load_trend_dataset(api_manager)
    data_logger.save_to_csv('data/top_50.csv')



# Input of the project:
run(sys.argv)
