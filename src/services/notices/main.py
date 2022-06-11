from src.drives.kafka import Kafka
from src.drives.enums import Topics
from src.drives.kafka_template import AbsctractKafka


def notify(notice):
    message = notice.value().decode('utf-8')
    queue = Kafka()
    queue.send_message(Topics.EMAIL, str(message))


def save(notice):
    print(f'Saving notice...')
    notify(notice)


def exec(message):
    print('Received message: {}'.format(message.value().decode('utf-8')))
    save(message)


def handler(queue: AbsctractKafka):
    queue.consume_from(topic=Topics.NEWS, exec=exec)


if __name__ == '__main__':
    handler(Kafka())
