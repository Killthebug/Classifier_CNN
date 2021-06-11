from google.api_core import timeout
from service.consumers import Consumer
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1


class GCPService(Consumer):
    def __init__(self, config=None):
        super().__init__()
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(
            config["project_id"], config["subscription_id"]
        )
        self.streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path, callback=self.callback
        )

    @staticmethod
    def callback(message):
        print(f"Received {message}.")
        message.ack()

    def consume(self):
        timeout = 5
        with self.subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                self.streaming_pull_future.result(timeout=timeout)
            except TimeoutError:
                self.streaming_pull_future.cancel()
