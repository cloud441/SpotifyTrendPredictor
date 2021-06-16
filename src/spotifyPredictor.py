#!/usr/bin/env python

import SpotifyAPI


def run():
    api_manager = SpotifyAPI.APIManager()
    if (api_manager.api):
        print(f'The API connection is established with user {api_manager.user}.')
    else:
        print(f'Error: Impossible to established API connection with user {api_manager.user}')



# Input of the project:
run()
