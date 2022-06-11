from confluent_kafka import Producer
from confluent_kafka import Consumer
from src.drives.enums import Topics

from src.drives.kafka_template import AbsctractKafka


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
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(
                msg.topic(), msg.partition()))

    def send_message(self, topic: Topics, message: str):
        print('Sending message...')

        self.producer.poll(0)
        self.producer.produce(topic.value, message.encode(
            'utf-8'), callback=self.delivery_report)
        print('End sending message...')

    def consume_from(self, topic: Topics, exec):
        self.consumer.subscribe([topic.value])

        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            exec(msg)
