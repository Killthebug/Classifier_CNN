import time
import json
from kafka import KafkaProducer
from service.producers import Producer


class KafkaService(Producer):
    def __init__(self, config: dict):
        super().__init__()
        self.client = KafkaProducer(
            bootstrap_servers=config["bootstrap_server"],
            value_serializer=self.value_serializer,
        )

    @staticmethod
    def value_serializer(data):
        return json.dumps(data).encode("utf-8")

    def produce(self, data, topic: str):
        data = {"number": data}
        print(self.client.send(topic, value=data))
        time.sleep(1)
