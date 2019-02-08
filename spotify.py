"""
This is a program that can interact with the Spotify API. More specifically it can connect to your specific account
and interact with your specific data. It can find your top ten songs and artists from 3 different time periods,
show how many followers you have, and show the song that is currently playing.

Sources:
Ian Annase
https://spotipy.readthedocs.io
"""

import json # Imported modules
import os
import webbrowser
import sys
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1] # takes user's username from terminal
spotify_data = 'user-top-read user-read-private user-read-playback-state' # parameters for which spotify data to access

try: # try and except for user authentification
    token = util.prompt_for_user_token(username, spotify_data, client_id = 'cc1f9fec3419460d957459229fcba1d8',
    client_secret = 'fd73664e0b1e4b1a9867cf3024990205', redirect_uri = 'http://google.com/'
    )
except (AttributeError, JSONDecodeError):
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username, spotify_data, client_id = 'cc1f9fec3419460d957459229fcba1d8',
    client_secret = 'fd73664e0b1e4b1a9867cf3024990205', redirect_uri = 'http://google.com/'
    )

spotipy = spotipy.Spotify(auth=token) # creates and instance of the spotipy object

while True: # loop that allows the user to choose a menu item multiple times
    user_object = spotipy.current_user() # creates current user object
    name = user_object['display_name'] # gets user's display name
    print() # Menu
    print('+--------------------------------+')
    print('Welcome to Spotipy ' + name + '!')
    print('+--------------------------------+')
    print('1 - Your top songs from last month')
    print('2 - Your top songs from last 6 months')
    print('3 - Your top songs of all time')
    print('4 - Your top artists from last month')
    print('5 - Your top artists from last 6 months')
    print('6 - Your top artists of all time')
    print('7 - See how many followers you have')
    print('8 - What song is currently playing?')
    print('9 - Exit')
    print()
    choice = input('Your choice: ')

    if choice == '1': # gets top ten songs from the past month
        print()
        print('Your Top Ten Songs From The Past Month')
        print('+------------------------------------+')
        top_tracks = spotipy.current_user_top_tracks(time_range='short_term', limit=10)
        for i, item in enumerate(top_tracks['items']):
            print(item['name'],'-', item['artists'][0]['name'])
        print()

    elif choice == '2': # gets top ten songs from the past 6 months
        print()
        print('Your Top Ten Songs From The Past 6 Months')
        print('+---------------------------------------+')
        top_tracks = spotipy.current_user_top_tracks(time_range='medium_term', limit=10)
        for i, item in enumerate(top_tracks['items']):
            print(item['name'],'-', item['artists'][0]['name'])
        print()

    elif choice == '3': # gets top ten songs from all time
        print()
        print('Your Top Ten Songs Of All Time')
        print('+----------------------------+')
        top_tracks = spotipy.current_user_top_tracks(time_range='long_term', limit=10)
        for i, item in enumerate(top_tracks['items']):
            print(item['name'],'-', item['artists'][0]['name'])
        print()

    elif choice == '4': # gets top ten artists from past month
        print()
        print('Your Top Ten Artists From The Past Month')
        print('+--------------------------------------+')
        top_artists = spotipy.current_user_top_artists(time_range='short_term', limit=10)
        for i, item in enumerate(top_artists['items']):
            print(item['name'])
        print()

    elif choice == '5': # gets top ten artists from past 6 months
        print()
        print('Your Top Ten Artists From The Past 6 Months')
        print('+-----------------------------------------+')
        top_artists = spotipy.current_user_top_artists(time_range='medium_term', limit=10)
        for i, item in enumerate(top_artists['items']):
            print(item['name'])
        print()

    elif choice == '6': # gets top ten artists from all time
        print()
        print('Your Top Ten Artists Of All Time')
        print('+------------------------------+')
        top_artists = spotipy.current_user_top_artists(time_range='long_term', limit=10)
        for i, item in enumerate(top_artists['items']):
            print(item['name'])
        print()

    elif choice == '7': # shows number of followers
        user_object = spotipy.current_user()
        num_followers = user_object['followers']['total']
        print()
        print('You have ' + str(num_followers) + ' followers!')
        print()

    elif choice == '8': # shows the currently playing track
        track_name = spotipy.current_user_playing_track()
        artist_name = track_name['item']['artists'][0]['name']
        track_name = track_name['item']['name']
        print()
        print('Current song: ' + track_name + ' - ' + artist_name)

    elif choice == '9': # exits program
        break
