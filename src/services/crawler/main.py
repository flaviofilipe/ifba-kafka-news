from src.drives.kafka import Kafka
from src.drives.enums import Topics
from src.drives.kafka_template import AbsctractKafka
from src.services.crawler.mock_notices import NOTICES


def handler(queue: AbsctractKafka):
    for notice in NOTICES:
        queue.send_message(Topics.NEWS, str(notice))


if __name__ == '__main__':
    handler(Kafka())
