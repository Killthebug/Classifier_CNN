import torch
import torchvision.transforms as transforms
from PIL import Image
from torch.autograd import Variable

PATH = "../models/lenet_trained.pt"
IMG_PATH = "../data/f_mnist_data/test/1/2.png"


def load_model(model_path: str) -> object:
    """
    Loads pretrained pytorch model
    :param model_path:
    :return:
    """
    model = torch.load(model_path)
    model.eval()
    return model


loader = transforms.Compose([transforms.Grayscale(num_output_channels=3), transforms.ToTensor()])


def image_loader(image_name: str) -> Variable:
    """
    Loads and transforms image given image filepath
    :param image_name:
    :return:
    """
    image = Image.open(image_name)
    image = loader(image).float()
    image = image.unsqueeze(0)
    return image


if __name__ == "__main__":
    inference_model = load_model(PATH)
    image = image_loader(IMG_PATH)
    result = inference_model(image)
    print(f'Image Class : {torch.argmax(result[0])}')