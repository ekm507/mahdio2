import numpy as np

def font1(frequency:float, duration:float, sampling_rate:float):

    time_domain = np.arange(0, duration, 1.0/sampling_rate)

    harmonics_sin = [
        (1, 1),
        (2, 0.2),
        (3, 0.7),
        (4, 0.5),
        (5, 0.2),
        (6, 0.1),
    ]

    frequency *= 2 * np.pi

    raw_note = np.sum([harmonic[1] * np.sin(harmonic[0] * frequency * time_domain) for harmonic in harmonics_sin], axis=0)

    min_amp = 0.04
    min_amp = 0.0
    max_amp = 0.4
    push_note = max_amp * np.exp(-time_domain / 2) * abs(np.cos(time_domain * 1) ) + min_amp

    full_note = raw_note * push_note * 0.2
    # full_note = raw_note

    # guard:
    full_note[full_note > max_amp] = max_amp
    full_note[full_note < -max_amp] = -max_amp

    return full_note



def font2(frequency:float, duration:float, sampling_rate:float):

    harmonics_sin=[
        (1, 0.2),
        (2, 0.8),
        (3, 0.5),
        (4, 0.1),
        (5, 0.05),
        (6, 0.02),
        (7, 0.01)
    ]

    time_domain = np.arange(0, duration, 1.0/sampling_rate)


    frequency *= 2 * np.pi
    min_amp = 0
    max_amp = 0.4

    raw_note = np.sum([harmonic[1] * np.sin(harmonic[0] * frequency * time_domain) for harmonic in harmonics_sin], axis=0)

    push_note = max_amp * np.cos(time_domain / 2 * 32) * np.exp(-time_domain * 1)

    full_note = raw_note * push_note
    # full_note = raw_note

    # guard:
    # full_note[full_note > max_amp] = max_amp
    # full_note[full_note < -max_amp] = -max_amp

    return full_note


def font3(frequency:float, duration:float, sampling_rate:float):

    time_domain = np.arange(0, duration, 1.0/sampling_rate)

    harmonics_sin = [
        (1, 1),
        (2, 0.2),
        (3, 0.7),
        (4, 0.5),
        (5, 0.2),
        (6, 0.1),
    ]

    frequency *= 2 * np.pi

    raw_note = np.sum([harmonic[1] * np.sin(harmonic[0] * frequency * time_domain) for harmonic in harmonics_sin], axis=0)

    min_amp = 0.04
    min_amp = 0.0
    max_amp = 0.4
    push_note = max_amp * np.exp(-time_domain * 3) 

    full_note = raw_note * push_note * 0.2
    # full_note = raw_note

    # guard:
    full_note[full_note > max_amp] = max_amp
    full_note[full_note < -max_amp] = -max_amp

    return full_note




def font4(frequency:float, duration:float, sampling_rate:float):

    time_domain = np.arange(0, duration, 1.0/sampling_rate)


    frequency *= 2 * np.pi

    raw_note = np.mod(time_domain, 1/frequency) * frequency * 0.4 - 0.2

    min_amp = 0.04
    min_amp = 0.0
    max_amp = 0.4

    full_note = raw_note * 1
    # full_note = raw_note

    # guard:
    # full_note[full_note > max_amp] = max_amp
    # full_note[full_note < -max_amp] = -max_amp

    return full_note



def font5(frequency:float, duration:float, sampling_rate:float):

    time_domain = np.arange(0, duration, 1.0/sampling_rate)


    frequency *= 2 * np.pi

    work_time = 0.5

    raw_note = np.floor(np.sin(time_domain * frequency) + work_time) * 0.4 - 0.2

    min_amp = 0.04
    min_amp = 0.0
    max_amp = 0.4

    full_note = raw_note * 1
    # full_note = raw_note

    # guard:
    # full_note[full_note > max_amp] = max_amp
    # full_note[full_note < -max_amp] = -max_amp

    return full_note


