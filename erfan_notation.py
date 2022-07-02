def erfan_note_to_note(notes_str : str, note_duration : float, main_note : int) -> list:

    notes_list = []
    time = 0
    note_elongation = 2
    for key in notes_str.split():
        if key != '-':
            try:
                note = (int(key) + main_note, time, note_duration * note_elongation, 100)
                notes_list.append(note)
            except:
                continue
        time += note_duration
    return notes_list
    