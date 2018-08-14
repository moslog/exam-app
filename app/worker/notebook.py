from app.assets import template
from .writer import write_notebook
from .image import images_name

def create_notebook(name, email, date):
    t = template
    t = t.replace('%name', name)
    t = t.replace('%email', email)
    t = t.replace('%date', date)
    for i in range(5):
        t = t.replace(f'%SOAL_{i+1}', images_name[i])
    name_without_space = name.replace(' ', '_')
    write_notebook(t, f'UJIAN_LOGIC_{name_without_space}.ipynb')