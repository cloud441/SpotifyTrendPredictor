#!/usr/bin/env python

import sys
import SpotifyAPI
import DataLog
from pprint import pprint


def run(argv):
    # Instance a Spotify API Manager:
    api_manager = SpotifyAPI.APIManager() if (len(argv[1:]) == 0) else SpotifyAPI.APIManager(user=argv[1])
    if not api_manager.api:
        print(f'Error: Impossible to established API connection with user {api_manager.user}')
        return

    print(f'\nThe API connection is established with user {api_manager.user}.\n')


    # Instance a Data Logger to store final dataset and apply pre-processing:
    data_logger = DataLog.DataLogger()
    data_logger.load_trend_dataset(api_manager)
    print(f'Data tracks is loaded from Spotify API.\n\n')


    # Apply pre-processing:
    pprint(data_logger.apply_pre_processing())

    # Save final dataset to CSV file needed by Azure:
    data_logger.save_to_csv('data/dataset.csv')
    print(f'\nFinal dataset in store at: data/dataset.csv')



# Input of the project:
run(sys.argv)
