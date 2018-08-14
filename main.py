from app.worker.notebook import create_notebook
from app.worker.image import create_image
from app.worker.writer import path

def run_generator():
    print('Aplikasi Generator Ujian Logic Pondok Programmer')
    name = input('Masukkan Nama Lengkap : ')
    email = input('Masukkan Email : ')
    
    from datetime import datetime
    now = datetime.now()
    months = [
        'Januari',
        'Februari',
        'Maret',
        'April',
        'Mei',
        'Juni',
        'Juli',
        'Agustus',
        'September',
        'Oktober',
        'November',
        'Desember'
    ]
    date = f'{now.day} {months[now.month - 1]} {now.year}'

    create_image()
    create_notebook(name, email, date)
    
    
def run_notebook():
    from subprocess import call
    call(['jupyter', 'notebook', path])


def run():
    run_generator()
    run_notebook()

run()