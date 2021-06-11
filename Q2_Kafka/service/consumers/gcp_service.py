from service.consumers import Consumer
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1


class GCPService(Consumer):
    """
    Consumer class to receive messages over Google Pub Sub.
    Inherits from parents Consumer class.
    """
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
        """
        Callback method required for Google Pub Sub
        :param message:
        """
        print(f"Received {message}.")
        message.ack()

    def consume(self):
        """
        Function to enable consumer to pull stream of data from message queue
        """
        timeout = 5
        with self.subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                self.streaming_pull_future.result(timeout=timeout)
            except TimeoutError:
                self.streaming_pull_future.cancel()
