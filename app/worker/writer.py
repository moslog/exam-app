import os
from subprocess import call
from pathlib import Path

home = str(Path.home())
path = f'{home}/Desktop/exam_files'
if os.path.exists(path):
    call(['rm', '-rf', path])
call(['mkdir', path])

def write_notebook(content, filename):
    assert('.ipynb' in filename)
    filename = f'{path}/{filename}'
    
    with open(filename, 'w') as fw:
        fw.write(content)
        print(f'Created : {filename}')

def write_image(byte_buffer, filename):
    assert('.png' in filename)
    filename = f'{path}/{filename}'
    with open(filename, 'wb') as fw:
        fw.write(byte_buffer)
        print(f'Created : {filename}')