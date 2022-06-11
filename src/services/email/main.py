from src.drives.kafka import Kafka
from src.drives.enums import Topics
from src.drives.kafka_template import AbsctractKafka


def exec(message):
    print('Received message: {}'.format(message.value().decode('utf-8')))


def handler(queue: AbsctractKafka):
    queue.consume_from(topic=Topics.EMAIL, exec=exec)


if __name__ == '__main__':
    handler(Kafka())
