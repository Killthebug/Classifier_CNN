import time
import json
from kafka import KafkaProducer
from service.producers import Producer


class KafkaService(Producer):
    """
    Producer class to send messages over Kafka.
    Inherits from parents Producer class.
    """
    def __init__(self, config: dict):
        super().__init__()
        self.client = KafkaProducer(
            bootstrap_servers=config["bootstrap_server"],
            value_serializer=self.value_serializer,
        )

    @staticmethod
    def value_serializer(data) -> json:
        """
        Helper method to serialize data as a JSON
        :param data:
        :return: json
        """
        return json.dumps(data).encode("utf-8")

    def produce(self, data, topic: str):
        """
        Function to enable Producer to send messages to a given topic
        :param data:
        :param topic:
        :return:
        """
        data = {"number": data}
        print(self.client.send(topic, value=data))
        time.sleep(1)
