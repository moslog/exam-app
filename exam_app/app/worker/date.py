from datetime import datetime

def resolve_date(date: datetime) -> str:
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
    res = f'{date.day} {months[date.month - 1]} {date.year}'
    return res