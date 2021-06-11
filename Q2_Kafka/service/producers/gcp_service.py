from google.cloud import pubsub_v1
from service.producers import Producer


class GCPService(Producer):
    def __init__(self, config: dict):
        super().__init__()
        self.project_id = config["project_id"]
        self.client = pubsub_v1.PublisherClient()

    @staticmethod
    def value_serializer(data):
        return str(data).encode("utf-8")

    def produce(self, data, topic):
        topic_path = self.client.topic_path(self.project_id, topic)
        serialized_data = self.value_serializer(data)
        future = self.client.publish(topic_path, serialized_data)
        print(future.result())
