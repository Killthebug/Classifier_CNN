from PIL import Image
from torch.autograd import Variable
from torchvision.transforms import transforms
import pickle
from service.producers.kafka_service import KafkaService as KProducer

"""
Todo:
Prior to running code ::
Configure PUBLISHER_SERVER AND PUBLISHER_TOPIC
"""
IMG_PATH = "../Q1_Mnist_CNN/data/f_mnist_data/test/1/2.png"
PUBLISHER_SERVER = "localhost:9092"
PUBLISHER_TOPIC = "test"


def image_loader(image_path: str) -> Variable:
    """
    Loads and transforms image given image filepath
    :param image_path:
    :return: Variable
    """
    loader = transforms.Compose([transforms.Grayscale(num_output_channels=3), transforms.ToTensor()])
    image = Image.open(image_path)
    image = loader(image).float()
    image = image.unsqueeze(0)
    return image


def value_serializer(data: object) -> pickle:
    return pickle.dumps(data)


def send_to_ml_service(image_path: str):
    image = image_loader(image_path)
    publisher_config = {
        "bootstrap_server": PUBLISHER_SERVER,
        "value_serializer": value_serializer,
    }
    client = KProducer(config=publisher_config)
    client.produce(image, PUBLISHER_TOPIC)
    print("Published to", PUBLISHER_SERVER, PUBLISHER_TOPIC)


if __name__ == "__main__":
    assert (len(PUBLISHER_SERVER) != 0 and len(PUBLISHER_TOPIC) != 0)
    for i in range(100):
        send_to_ml_service(IMG_PATH)
