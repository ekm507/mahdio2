#!/usr/bin/python3

import music
from write import write_to_file
from read_midi import read_midi, read_midi_tracks
import sys
import fonts

filename = sys.argv[1]


notes_list = [
    (70, 0, 1, 1),
    (70, 0.1, 1, 1),
    (75, .2, 1, 1),
    (75, .3, 1, 1),
    (76, .4, 1, 1),
    (76, .5, 1, 1),
    (75, .6, 2, 1),
]

notes_list = [
    (70, 0, 8, 100),
    (78, 2, 8, 100),
    (86, 4, 8, 100),
    (94, 6, 8, 100),
]

notes_str = '''
7 9 7 - 7 - 7 - 
9 11 9 - 9 - 9 - 
11 9 7 - 7 - 7 - 
7 9 7 - 7 - 7 - 
7 6 4 - 4 - 4 - 
6 7 6 - 6 - 6 - 
6 4 2 - 2 - 2 - 
4 6 4 - 4 - 4 - 
4 2 1 - 1 - 1 - 
2 4 1 -'''
from erfan_notation import erfan_note_to_note
notes_list = erfan_note_to_note(notes_str, 0.5, 70)

audio_wave = music.music_1channel_synthesis(notes_list, fonts.font3, time_type='independant')

print("normalizing")
audio_wave *= 0.01
write_to_file(list(audio_wave), filename='test.wav')
