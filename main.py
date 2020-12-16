#!/usr/bin/env python

import pafy , art , socket


def phelp():
    input('''This program can run on windows as well as linux and possibly on mac(not tested).\nIt can be used to download youtube videos and playlists''')

def url_error():
    input('''Sorry either the requested video/playlist's url is incorrect , or it cant be downloaded''')

def user():
    art.tprint('Pydownloader')
    print('by: Tatva Agarwal')
    choice = int(input('''Please enter your choice:
                      [1] Download a video
                      [2] Download a whole playlist
                      [3] Print Help\n>'''))
    if choice == 1:
        url = input('''Please enter the url of the video\n>''')
    elif choice == 2:
        url = input('''Please enter the url of a Playlist\n>''')
    elif choice == 3:
        phelp()
    else:
        url_error()
    if (choice == 1 or choice == 2) and url != '':
        return url , choice
    else:
        url_error()

def internet():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

def connection_stream():
    print('Checking internet connection...')
    if internet() == True:
        print('Internet available , getting video data...')
        get_streams()
    else:
        print('Internet not available , please check your connection')

def get_streams_vid(url):
    pass


def main():
    url , choice = user()


    
    


    


