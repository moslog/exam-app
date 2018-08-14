from datetime import datetime
from .app.worker.notebook import create_notebook
from .app.worker.image import create_image
from .app.worker.writer import path
from .app.worker.date import resolve_date

def run_generator():
    print('Aplikasi Generator Ujian Logic Pondok Programmer')
    name = input('Masukkan Nama Lengkap : ')
    email = input('Masukkan Email : ')
    date = resolve_date(datetime.now())
    
    create_image()
    create_notebook(name, email, date)
    
    
def run_notebook():
    from subprocess import call
    call(['jupyter', 'notebook', path])


def run():
    run_generator()
    run_notebook()