import subprocess
import os.path


def run(input_url):
    '''
    Play media file using `ffplay`:
        input_url - full path to file
    '''
    if not os.path.isfile(input_url):
        print('404 file does not exist')
        return

    command = f'.\\ffplay -i {input_url}'
    subprocess.call(command)
