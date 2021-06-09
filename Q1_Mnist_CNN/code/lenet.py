"""
Implementation of the Lenet-5 network for image classification as proposed in
“Gradient-Based Learning Applied To Document Recognition"
-Yann LeCun, Leon Bottou, Yoshua Bengio, and Patrick Haffner
"""

import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    def __init__(self, numberOfClasses):
        super().__init__()

        self.cnn_model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=6, kernel_size=5),  # (N, 1, 28, 28) -> (N, 6, 24, 24)
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2, stride=2),  # (N, 6, 24, 24) -> (N, 6, 12, 12)
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5),  # (N, 6, 12, 12) -> (N, 6, 8, 8)
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2, stride=2),  # (N, 6, 8, 8) -> (N, 16, 4, 4)
        )

        self.fc_model = nn.Sequential(
            nn.Linear(in_features=256, out_features=120),  # (N, 256) -> (N, 120)
            nn.Tanh(),
            nn.Linear(in_features=120, out_features=84),  # (N, 120) -> (N, 84)
            nn.Tanh(),
            nn.Linear(in_features=84, out_features=numberOfClasses)  # (N, 84)  -> (N, #ofclasses))
        )

    def init(self):
        super(LeNet, self).init()

    def forward(self, x):
        x = self.cnn_model(x)
        x = x.view(x.size(0), -1)
        logits = self.fc_model(x)
        probs = F.softmax(logits, dim=1)
        return logits, probs
