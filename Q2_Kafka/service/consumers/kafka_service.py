from service.consumers import Consumer
from kafka import KafkaConsumer
import json


class KafkaService(Consumer):
    """
    Consumer class to send messages over Kafka.
    Inherits from parents Consumer class.
    """
    def __init__(self, config=None):
        super().__init__()
        self.client = KafkaConsumer(
            config["name"],
            bootstrap_servers=config["bootstrap_server"],
            auto_offset_reset=config["auto_offset_reset"],
            enable_auto_commit=config["enable_auto_commit"],
            group_id=config["group_id"],
            value_deserializer=config["value_deserializer"],
        )

    def consume(self):
        """
        Function to enable consumer to pull stream of data from message queue
        """
        for message in self.client:
            # print(f"{message} added")
            return message
