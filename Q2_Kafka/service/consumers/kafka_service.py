from service.consumers import Consumer
from kafka import KafkaConsumer
import json


class KafkaService(Consumer):
    def __init__(self, config=None):
        super().__init__()
        self.client = KafkaConsumer(
            config["name"],
            bootstrap_servers=config["bootstrap_server"],
            auto_offset_reset=config["auto_offset_reset"],
            enable_auto_commit=config["enable_auto_commit"],
            group_id=config["group_id"],
            value_deserializer=self.value_deserializer,
        )

    @staticmethod
    def value_deserializer(data):
        return json.loads(data.decode("utf8"))

    def consume(self):
        for message in self.client:
            print(f"{message} added")
