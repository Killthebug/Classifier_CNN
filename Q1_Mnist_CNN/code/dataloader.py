"""
Dataloader function responsible for downloading the MNIST Fashion Dataset
and transforming it.
"""

import torchvision
import torchvision.transforms as transforms
import torch

trainset = torchvision.datasets.FashionMNIST(root="./../data", train=True, download=True, transform = transforms.ToTensor())
testset = torchvision.datasets.FashionMNIST(root="./.../data", train=False, download=True, transform = transforms.ToTensor())

trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False)

# Put enforcer around data layer
