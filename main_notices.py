import ast
import logging
import logging.config

from src.drives.kafka import Kafka
from src.drives.enums import Topics
from src.drives.kafka_template import AbsctractKafka
from src.repository import create_notice, find_notice_by_title
from src.utils import format_date

logging.config.fileConfig('logging.conf')
log = logging.getLogger('mainNotices')


def notify(message):
    message = message.value().decode('utf-8')
    queue = Kafka()
    queue.send_message(Topics.EMAIL, str(message))


def save(message):
    log.info(f'Saving notice...')
    notice = ast.literal_eval(message.value().decode('utf-8'))
    notice['date'] = format_date(notice['date'])

    if len(find_notice_by_title(notice['title'])):
        return

    create_notice(notice)
    notify(message)


def exec(message):
    log.info('Exec...')
    try:
        notice = ast.literal_eval(message.value().decode('utf-8'))
        log.info('Received message: {}'.format(notice['title']))
        save(message)
    except Exception as err:
        log.error('Error to save message: {}'.format(message.value()))


def handler(queue: AbsctractKafka):
    log.info('handler...')
    queue.consume_from(topic=Topics.NEWS, exec=exec)


if __name__ == '__main__':
    log.info('Starting...')
    handler(Kafka())
    log.info("Finished...")
