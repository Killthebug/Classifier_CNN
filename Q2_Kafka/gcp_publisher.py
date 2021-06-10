from google.cloud import pubsub_v1
#
# # TODO(developer)
# project_id = "silver-spark-316405"
# topic_id = "sending_topic_1"
#
# publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
# # topic_path = publisher.topic_path(project_id, topic_id)
#
# for n in range(1, 10):
#     data = "Message number {}".format(n)
#     # Data must be a bytestring
#     data = data.encode("utf-8")
#     # When you publish a message, the client returns a future.
#     future = publisher.publish(topic_path, data)
#     print(future.result())
#
# print(f"Published messages to {topic_path}.")
#


class MyPubSubProducer:
    def __init__(self, project_id):
        self.project_id = project_id
        self.publisher = pubsub_v1.PublisherClient()

    @staticmethod
    def value_serializer(data):
        return data.encode('utf-8')

    def send_data(self, data, topic):
        topic_path = self.publisher.topic_path(self.project_id, topic)
        serialized_data = self.value_serializer(data)
        future = self.publisher.publish(topic_path, serialized_data)
        print(future.result())



