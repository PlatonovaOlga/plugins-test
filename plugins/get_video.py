import subprocess


def run(input_url):
    '''
    Extract a video stream from media using `ffmpeg`

    Arguments:
        input_url - full path to file
    '''
    command = f'.\\ffmpeg -i {input_url} -map 0:1 output.mp4'

    subprocess.call(command)
    