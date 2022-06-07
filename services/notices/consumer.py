from kafka import KafkaConsumer

TOPIC_NEWS='news'
consumer = KafkaConsumer(TOPIC_NEWS)

for msg in consumer:
    print (msg)