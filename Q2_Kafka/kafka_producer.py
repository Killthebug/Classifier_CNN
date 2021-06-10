import time
from json import dumps
from kafka import KafkaProducer


class MyKafkaProducer:

    def __init__(self, bootstrap_server: str):
        self.bootstrap_server = bootstrap_server
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_server,
                                      value_serializer=self.value_serializer)

    @staticmethod
    def value_serializer(data):
        return dumps(data).encode('utf-8')

    def send_data(self, data, topic: str):
        data = {'number': data}
        print(self.producer.send(topic, value=data))
        time.sleep(1)


