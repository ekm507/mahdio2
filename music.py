import notes
from midi_conversions import convert_notes_types_to_freq
import numpy as np
import sys


# this should do with new version of notes only.
"""
    note version 2 is a list of tuples. each element of tuple is like this:
    (note number, note start time, note duration, note velocity)

    note number: usually midi number of note, but can also be frequency in float or note name in string)
    note start time: this can be relative or independant timing.
    note duration: how long a note should be present despite what amplitude envelope function it uses.
    note velocity: amplitude of a note. how hard a note is being played
"""


def create_music(tracks, fonts, sampling_rate: float = 48000,
                             note_type: str = 'midi', time_type='relative'):
    audio_channels = []
    for track_number, track in enumerate(tracks):
        print(f'generating track {track_number}')
        if len(track) > 0:
            audio_channels.append(
                music_1channel_synthesis(track, fonts[track_number], sampling_rate=sampling_rate, note_type=note_type, time_type=time_type)
                )

    max_len = max(list(map(lambda x:len(x), audio_channels)))
    # max_len = len(audio_channels[0])
    audio_mixed = np.zeros(max_len, np.float64)

    for channel in audio_channels:
        audio_mixed[:len(channel)] += channel
    
    return audio_mixed


def music_1channel_synthesis(notes_list, font, sampling_rate: float = 48000,
                             note_type: str = 'midi', time_type='relative'):  # for notes list version3

    print('generating notes')

    notes_list = convert_notes_types_to_freq(notes_list, note_type)

    notes_set = notes.generate_note_dict_by_list(
        notes_list, font, sampling_rate)


    max_note_duration = max(list(k[2] for k in notes_list))
    
    # how long music will be
    if time_type == 'relative':
        note_duration = max(list(k[1] for k in notes_list))
        track_duration = sum(list(k[1] for k in notes_list)) + note_duration
    elif time_type == 'independant':
        track_duration = max(list(k[1] for k in notes_list)) + max_note_duration


    track = np.zeros((int(track_duration * sampling_rate) + 1), np.float64)

    print('syntesising music')
    k = 0
    # now that notes are generated, we are to mix them.
    if time_type == 'independant':
        for note, time, duration, velocity in notes_list:
            k += 1
            sys.stdout.write(repr(k))
            sys.stdout.write('\n')
            sys.stdout.write('\x1b[3D\x1b[1A')

            t1 = int (time * sampling_rate)
            t2 = int (duration * sampling_rate)

            track[t1: t1 + t2] += notes_set[note][:t2] * velocity
    
    return track

