import logging
from confluent_kafka import Producer
from confluent_kafka import Consumer
from src.drives.enums import Topics

from src.drives.kafka_template import AbsctractKafka

log = logging.getLogger(__name__)


class Kafka(AbsctractKafka):
    def __init__(self) -> None:
        super().__init__()
        self.consumer = Consumer({
            'bootstrap.servers': self.server,
            'group.id': 'mygroup',
            'auto.offset.reset': 'earliest'
        })

        self.producer = Producer({'bootstrap.servers': self.server})

    def delivery_report(self, err, msg):
        if err is not None:
            log.error('Message delivery failed: {}'.format(err))
        else:
            log.info('Message delivered to {} [{}]'.format(
                msg.topic(), msg.partition()))

    def send_message(self, topic: Topics, message: str):
        log.info('Sending message...')
        log.info(f'Topic: {topic.value}')

        self.producer.produce(topic.value, message.encode(
            'utf-8'), callback=self.delivery_report)
        self.producer.poll(1)
        log.info('End sending message...')

    def consume_from(self, topic: Topics, exec):
        self.consumer.subscribe([topic.value])
        log.info(f'Topic: {topic.value}')

        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                log.info('Mensage is none...')
                continue
            if msg.error():
                log.info("Consumer error: {}".format(msg.error()))
                continue

            exec(msg)
