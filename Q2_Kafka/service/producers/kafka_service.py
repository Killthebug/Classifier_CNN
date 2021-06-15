import time
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
            value_serializer=config["value_serializer"],
        )

    def produce(self, data, topic: str):
        """
        Function to enable Producer to send messages to a given topic
        :param data:
        :param topic:
        :return:
        """
        data = {"number": data}
        print(data)
        print(self.client.send(topic, value=data))
        time.sleep(1)
