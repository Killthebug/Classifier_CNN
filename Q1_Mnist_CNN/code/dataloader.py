"""
Dataloader function responsible for downloading the MNIST Fashion Dataset
and transforming it.
"""

import torchvision
import torchvision.transforms as transforms
from torchvision import datasets
import torch


def loadData(train_data_path: str, test_data_path: str) -> (object, object):
    train_dataset = datasets.ImageFolder(train_data_path, transform=transforms.ToTensor())
    test_dataset = datasets.ImageFolder(test_data_path, transform=transforms.ToTensor())

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=4, shuffle=False)

    return train_loader, test_loader
