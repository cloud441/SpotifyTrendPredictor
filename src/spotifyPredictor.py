#!/usr/bin/env python

import sys
import SpotifyAPI


def run(argv):

    api_manager = SpotifyAPI.APIManager() if (len(argv[1:]) == 0) else SpotifyAPI.APIManager(user=argv[1])
    if (api_manager.api):
        print(f'The API connection is established with user {api_manager.user}.')
        api_manager.get_new_released()
    else:
        print(f'Error: Impossible to established API connection with user {api_manager.user}')



# Input of the project:
run(sys.argv)
