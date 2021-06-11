from google.cloud import pubsub_v1
from service.producers import Producer


class GCPService(Producer):
    """
    Producer class to send messages over Google Pub Sub.
    Inherits from parents Producer class.
    """
    def __init__(self, config: dict):
        super().__init__()
        self.project_id = config["project_id"]
        self.client = pubsub_v1.PublisherClient()

    @staticmethod
    def value_serializer(data) -> bytes:
        """
        Helper method to serialize data as bytes
        :param data:
        :return: json
        """
        return str(data).encode("utf-8")

    def produce(self, data, topic):
        """
        Function to enable Producer to send messages to a given topic
        :param data:
        :param topic:
        :return:
        """
        topic_path = self.client.topic_path(self.project_id, topic)
        serialized_data = self.value_serializer(data)
        future = self.client.publish(topic_path, serialized_data)
        print(future.result())
