import subprocess


def run(input_url):
    '''
    Extract per-frame information for a first video stream 
    into a json file using 'ffprobe'

    Arguments:
        input_url - full path to file
    '''
    with open("info.json", "w") as f:
        command = f'.\\ffprobe -select_streams v:0 -print_format json -show_frames -i {input_url}'
    
    subprocess.call(command, stdout=f)
        
    