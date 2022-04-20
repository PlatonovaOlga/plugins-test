"""
Extract a video stream from media using `ffmpeg`

Arguments:
    input_url - full path to file
"""
import os
import subprocess


def _get_video(input_path, output_name):
    command = f'.\\ffmpeg -i {input_path} -map 0:1 {output_name}'

    subprocess.call(command)
    

def main(options):
    if not options:
        print('Please, input path to file')
        return
        
    input_path = options.split(' ')[0]
    input_name = os.path.basename(input_path)

    output_name = f'only_video_{input_name}'
    output_path = input_path.replace(
        input_name, 
        output_name)

    _get_video(input_path, output_name)
    print(f'Path to result file: {output_path}')
