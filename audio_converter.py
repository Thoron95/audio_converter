'''
A script that convert and audio file from one format to another using `pydub` library.
'''

from pydub import AudioSegment
import argparse
import os

#Dictionary of formats to which script can convert to.
ACCEPTED_FORMATS = {
    '1' : 'ogg',
    '2' : 'wav',
    '3' : 'mp3',
    '4' : 'mp4',
    '5' : 'flv'
}

#Taking path to file as argument
parser = argparse.ArgumentParser(description='Convert ffmpeg video file into a specified format audio file.')
parser.add_argument('file', metavar='file', help='A path to your file')
args = parser.parse_args()

#Checking if provided path to file is valid
path = args.file
if not os.path.exists(path):
    print('File not found')
    exit()

#Extract filename and extension from path
file_name = path.split('\\')[-1].split('.')[:-1]
file_name = ''.join(file_name)
file_ext = path.split('\\')[-1].split('.')[-1]
file_ext = ''.join(file_ext)

#Try to create instance of AudioSegment from file
try:
    audio_file = AudioSegment.from_file(path, file_ext)
except FileNotFoundError:
    print("Couldn't find ffprobe.exe or ffmpeg.exe.")
    print("Make sure those files are in the same folder as script.")

#Print out informations about the file and get desired_format(hopefully from the list)
print(f'File: {file_name}')
print(f'Current format: {file_ext}')
print('\nWhich format would you like to convert to?')
desired_format = input('<< 1. ogg | 2. wav | 3. mp3 | 4. mp4 | 5. flv >>\n')

#Checking if file format provided is on the list. If so the conversion is performed
output_format = None
for key in ACCEPTED_FORMATS:
    if desired_format == key:
        output_format = ACCEPTED_FORMATS[key]
        output_filename = file_name + '.' + output_format
        audio_file.export(output_filename, format=output_format)
    elif desired_format.lower() == ACCEPTED_FORMATS[key]:
        output_format = ACCEPTED_FORMATS[key]
        output_filename = file_name + '.' + output_format
        audio_file.export(output_filename, format=output_format)

#Print out the results
if output_format:
    print(f'File has been saved as {output_filename}')
else:
    print('File format you provided is not accepted by this script.')