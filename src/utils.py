
from datetime import datetime
import logging

log = logging.getLogger(__name__)


def format_date(date: str) -> str:
    log.info('Formating date...')
    date, hour = date.replace('h', ':').split(' ')

    date = list(map(int, date.split('/')))
    hour = list(map(int, hour.split(':')))

    date_formatted = datetime(date[2], date[1], date[0], hour[0], hour[1])
    return date_formatted
