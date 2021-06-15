from service.producers.kafka_service import KafkaService as KProducer
from service.consumers.kafka_service import KafkaService as KConsumer

import torch
import pickle
import json

MODEL_PATH = "../Q1_Mnist_CNN/models/lenet_trained.pt"

PUBLISHER_SERVER = "localhost:9092"
PUBLISHER_TOPIC = "test_response"

SUBSCRIBER_SERVER = "localhost:9092"
SUBSCRIBER_TOPIC = "test"


def load_model(model_path: str) -> object:
    """
    Loads pretrained pytorch model
    :param model_path:
    :return:
    """
    model = torch.load(model_path)
    model.eval()
    return model


def inference_on_data(image):
    result = inference_model(image)
    class_label = torch.argmax(result[0])
    # Print to log acts as a proxy of saving to an actual DB
    print(f'Image Class : {class_label}')
    return str(class_label)


def publish_response(class_label):
    client = KProducer(config=publisher_config)
    client.produce(class_label, PUBLISHER_TOPIC)


def enable_subscription():
    client = KConsumer(config=subscriber_config)
    counter = 0
    while 1:
        data = client.consume()
        if data:
            print("Received Data", counter)
            class_label = inference_on_data(data.value)
            publish_response(class_label)


def kafka_serializer(data):
    """
    Serializer used by the Producer Service to send class_label to subscribers.
    class_label is generated by inferring on image using pre-trained lenet
    :param data:
    :return:
    """
    return json.dumps(data).encode('utf-8')


def kafka_deserializer(data):
    """
    Deserializer used by the Consumer Service to parse images sent to the model
    :param data:
    :return:
    """
    return pickle.loads(data)


if __name__ == "__main__":

    subscriber_config = {
        "name": SUBSCRIBER_TOPIC,
        "bootstrap_server": SUBSCRIBER_SERVER,
        "value_deserializer": kafka_deserializer,
        "auto_offset_reset": "earliest",
        "enable_auto_commit": True,
        "group_id": "counters",
    }

    publisher_config = {
        "bootstrap_server": PUBLISHER_SERVER,
        "value_serializer": kafka_serializer,
    }

    inference_model = load_model(MODEL_PATH)
    enable_subscription()
