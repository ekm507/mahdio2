import sys

def create_note_list(font, note_frequency_list, duration, sampling_rate,):

    note_list = [
        font(frequency, duration, sampling_rate)
        for frequency in note_frequency_list
    ]
    return note_list


def generate_note_dict_by_list(notes_list, font, sampling_rate) -> dict:
    frequency_set = set()
    duration_max = 0
    for frequency, _, duration, _ in notes_list:
        duration_max = max(duration_max, duration)
        frequency_set.add(frequency)
    
    frequency_list = list(frequency_set)
    
    generated_note_list = create_note_list(font, frequency_list, duration_max, sampling_rate)
    generated_note_dict = dict(zip(frequency_list, generated_note_list))
    return generated_note_dict
