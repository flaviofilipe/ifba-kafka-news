import json
from kafka import KafkaProducer


TOPIC_NEWS = 'news'

producer = KafkaProducer(
    bootstrap_servers=['broker:9092'],
    api_version=(0, 11, 5),
)

print('Sending message...')
producer.send(TOPIC_NEWS, b'some_message_bytes')
producer.flush()

print('End producer...')