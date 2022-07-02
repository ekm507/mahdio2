#!/usr/bin/python3

import music
from write import write_to_file
from read_midi import read_midi, read_midi_tracks
import sys
import fonts

filename = sys.argv[1]

tracks = read_midi_tracks(filename)

# notes_list = read_midi(filename)

fonts = [
    fonts.font1,
    fonts.font2,
    fonts.font3,
    fonts.font4,
    fonts.font5,
    fonts.font1,
    fonts.font2,
    fonts.font3,
    fonts.font4,
    fonts.font5,
]

# audio_wave = music.music_1channel_synthesis(notes_list, fonts.font3, time_type='independant')
audio_wave = music.create_music(tracks, fonts, time_type='independant')

print("normalizing")
audio_wave *= 0.01

write_to_file(list(audio_wave), filename='test.wav')
