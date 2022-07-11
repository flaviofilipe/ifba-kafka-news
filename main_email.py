import ast
from src.drives.kafka import Kafka
from src.drives.enums import Topics
from src.drives.kafka_template import AbsctractKafka


def exec(message):
    notice = ast.literal_eval(message.value().decode('utf-8'))
    print(f'[Notify] New Notice: {notice["title"]}')


def handler(queue: AbsctractKafka):
    queue.consume_from(topic=Topics.EMAIL, exec=exec)


if __name__ == '__main__':
    handler(Kafka())
