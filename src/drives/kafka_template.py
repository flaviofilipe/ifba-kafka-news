from abc import ABC, abstractmethod
from typing import Callable

from src.drives.enums import Topics


class AbsctractKafka(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.server = 'localhost:9092'


    @abstractmethod
    def delivery_report(self, err, msg):
        pass

    @abstractmethod
    def send_message(self, topic: Topics, message: str):
        pass

    @abstractmethod
    def consume_from(self, topic: Topics, exec):
        pass
