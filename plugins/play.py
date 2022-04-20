"""
Play media file using `ffplay`. 
Plugin checks is file exists and
run all accepted options as subprocess.
    'file_name.mp4 -an -fs'
"""
import subprocess
import os.path


def _check(input_url):
    return os.path.isfile(input_url)


def _play(options):
    command = f'.\\ffplay -i {options}'
    subprocess.call(command)


def main(options):
    if not options:
        print('Please, input path to file')
        return
    input_url = options.split(' ')[0]
    if _check(input_url):
        _play(options)

    