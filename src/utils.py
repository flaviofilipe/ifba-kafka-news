
from datetime import datetime

def format_date(date: str) -> str:
    print('formatting')
    date, hour = date.replace('h', ':').split(' ')
    
    date = list(map(int, date.split('/')))
    hour = list(map(int, hour.split(':')))
    
    date_formatted = datetime(date[2], date[1], date[0], hour[0], hour[1])
    return date_formatted