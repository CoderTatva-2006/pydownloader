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

def connection_stream(url , choice):
    print('Checking internet connection...')
    if internet() == True:
        print('Internet available , getting video data...')
        if choice == 1:
            get_streams_vid(url)
        elif choice == 2:
            playlist_handle(url)
        else:
            pass
    else:
        print('Internet not available , please check your connection')

def get_streams_vid(url):
    vid = pafy.new(url)
    st = vid.allstreams
    for x in range(len(st)):
        print(f'[{x}] :- {st[x]} ')
    given = int(input('Please enter the desired quality\n>'))
    if str(input('Do you want to download the video[Y/N]')).upper() == 'Y':
        extension = str(vid.allstreams[given])[0:str(vid.allstreams[given]).find('@')]
        extension = extension[extension.find(':')+1:]
        vid.allstreams[given].download(f'./../videos/{vid.title}.{extension}')

def playlist_handle(url):
    playlist_list = pafy.get_playlist(url)
    for x in range(len(playlist_list)):
        vid = playlist['items'][x]['pafy']
        st = vid.allstreams
        for a in range(len(st)):
            print(f'[{x}] :- {st[x]} ')
        given = int(input('Please enter the desired quality\n>'))
        if str(input('Do you want to download the video[Y/N]')).upper() == 'Y':
            extension = str(vid.allstreams[given])[0:str(vid.allstreams[given]).find('@')]
            extension = extension[extension.find(':')+1:]
            vid.allstreams[given].download(f'./videos/{playlist_list["title"]}/{vid.title}.{extension}')

def main():
    url , choice = user()
    
    connection_stream(url , choice)
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram ended by user')
    except:
        print('Fatal Error')
    
    


    


