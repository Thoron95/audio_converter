# audio_converter
 
 A simple script that convert audio files.

 It requires "pydub" library which you can get by using:
 `pip install pydub`

 It takes path to a file as argument or if the file is in the same folder as script, just the name of a file.
 Path to a file must be provided in quotation marks and must have a file extension specified.
 For example "my_file" wont work while "my_file.mp4" will.
 
 **NOTE:** "ffmpeg.exe" and "ffprobe.exe" must be in the same folder as audio_converter.py (pydub reasons...)
 
 An examples of how to use script:
 `python audio_converter.py "my_audio_file.mp4"`
 `python audio_converter.py "C:\Users\User_name\Music\audio_file.wav"`