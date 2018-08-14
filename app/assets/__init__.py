import os
dir_path = os.path.dirname(os.path.realpath(__file__))

question_images = []
for package in 'ABCDE':
    with open(f'{dir_path}/q{package}.b64') as fr:
        images = [line for line in fr.readlines()]
        question_images.append(images)


template = ''
with open(f'{dir_path}/template.ipynb') as fr:
    template = fr.read()