'''
Extract per-frame information for a first video stream 
into a json file using 'ffprobe'

Arguments:
    input_url - full path to file
'''
import os
import subprocess


def _get_info(json_name, input_url):
    with open(json_name, "w") as f:
        command = f'.\\ffprobe -select_streams v:0 -print_format json -show_frames -i {input_url}'

        subprocess.call(command, stdout=f)


def main(options):
    if not options:
        print('Please, input path to file')
        return

    input_url = options.split(' ')[0]
    json_name = 'info_' + os.path.basename(input_url) + '.json'
    _get_info(json_name, input_url)
        
    