#!/usr/bin/env python

import sys
import SpotifyAPI
import DataLog
from pprint import pprint


def run(argv):

    api_manager = SpotifyAPI.APIManager() if (len(argv[1:]) == 0) else SpotifyAPI.APIManager(user=argv[1])
    if not api_manager.api:
        print(f'Error: Impossible to established API connection with user {api_manager.user}')
        return

    print(f'\nThe API connection is established with user {api_manager.user}.\n')
    data_logger = DataLog.DataLogger()
    data_logger.load_trend_dataset(api_manager)

    pprint(data_logger.apply_pre_processing())

    data_logger.save_to_csv('data/top_50_bis.csv')



# Input of the project:
run(sys.argv)
