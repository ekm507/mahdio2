# MahdiO 2: generate music

Generate music sound effects using mathematics.



# new method

instrument is not independant from note.

there is a font. which contains of instrument data including harmonics and push function. all is in numpy.  
to generate a note, you multiply arrays of sin function with harmonics and sum them up. then generate an array of push function with the same method and finally multiply two arrays together.

any font can have optional parameters. for example for changing frequency over time. this is however, not implemented yet.

## how to use
for testing, use like this:

```bash
./audio.py midi_file.mid
```

it will create a wav file you can play using your audio player application.

## files in this repo

* `functions.py` for some basic functions.
* `notes.py` for generating notes.
* `midi_conversions.py` for converting note number to frequency.
* `fonts.py` for describing each instrument and music font.
* `music.py` for generating music.
* `write.py` for writing generated audio into a wave file
* `read_midi.py` for reading notes data from `.mid` files
* `audio.py` for test.
## TODO

1. add TODOs here.
2. write a better README.md