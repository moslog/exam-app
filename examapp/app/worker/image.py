import base64
import hashlib
from app.assets import question_images
from .writer import write_image
from random import randint

images_name = []

def create_image():
    m = hashlib.md5()
    for (i, package) in enumerate(question_images):
        r = randint(0, len(package[i]) - 1) % 5
        image_str = package[r].replace('\n', '')
        data = base64.b64decode(image_str)
        m.update(data)
        name = f'{m.hexdigest()}.png'
        images_name.append(name)
        write_image(data, name)