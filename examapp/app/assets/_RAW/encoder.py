
print("*.b64 file should be put in parent directory -- assets/ --")
print("it must be done manually")
if input("[y / n] ") != 'y':
    exit()

import glob

folders = glob.glob('**/')

for folder in folders:
    
    folder_name = folder.replace('/','')
    b64file = f'q{folder_name}.b64'
    with open(b64file, 'a') as f:
        
        files = glob.glob(f'{folder}*.png')

        print(f'Writing for {b64file} has been started')

        for file in files:
            with open(file, 'rb') as img:
                import base64
                b64string = base64.b64encode(img.read())

                print(f'Write {file}')

                f.write(b64string.decode('utf-8'))
                if not any(x in file for x in ['05','10', '15', '20', '25']):
                    print('Append new line')
                    f.write('\n')
