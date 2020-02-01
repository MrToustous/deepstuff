import pandas as pd


def id_path(song_id: int = None):
    id_str = str(song_id)
    song_number = id_str
    for i in range(6-len(song_number)):
        song_number = '0' + song_number
    file_number = id_str[:-3]
    for i in range(3-len(file_number)):
        file_number = '0' + file_number
    return file_number + '/' + song_number + '.mp3'
