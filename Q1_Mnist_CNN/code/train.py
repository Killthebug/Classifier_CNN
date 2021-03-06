"""
Primary training script
"""

from datetime import datetime
from dataloader import loadData
import lenet
import torch
import torch.nn as nn
from torch import optim

NUMBER_OF_CLASSES = 10
RANDOM_SEED = 42
LEARNING_RATE = 0.001
BATCH_SIZE = 32
N_EPOCHS = 1
IMG_SIZE = 32

PATH = "../models/lenet_trained.pt"
TRAIN_DATA_PATH = "../data/f_mnist_data/train"
TEST_DATA_PATH = "../data/f_mnist_data/test"


def detect_gpu():
    """
    Helper function to check if GPU is available for training
    """
    train_target = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(train_target)
    return train_target


def train(train_loader: object, model: object, criterion: object, optimizer:object, device: str) -> \
        (object, object, float):
    """
    Single loop step while training
    """

    model.train()
    running_loss = 0

    for X, y_true in train_loader:
        optimizer.zero_grad()

        X = X.to(device)
        y_true = y_true.to(device)

        # Forward pass
        y_hat, _ = model(X)
        loss = criterion(y_hat, y_true)
        running_loss += loss.item() * X.size(0)

        # Backward pass
        loss.backward()
        optimizer.step()

    epoch_loss = running_loss / len(train_loader.dataset)
    return model, optimizer, epoch_loss


def validate(valid_loader: object, model: object, criterion: object, device: str) -> (object, float):
    """
    Function for the validation step of the training loop
    """

    model.eval()
    running_loss = 0

    for X, y_true in valid_loader:
        X = X.to(device)
        y_true = y_true.to(device)

        # Forward pass and record loss
        y_hat, _ = model(X)
        loss = criterion(y_hat, y_true)
        running_loss += loss.item() * X.size(0)

    epoch_loss = running_loss / len(valid_loader.dataset)

    return model, epoch_loss


def get_accuracy(model: object, data_loader: object, device: str) -> float:
    """
    Function for computing the accuracy of the predictions over the entire data_loader
    """

    correct_pred = 0
    n = 0

    with torch.no_grad():
        model.eval()
        for X, y_true in data_loader:
            X = X.to(device)
            y_true = y_true.to(device)

            _, y_prob = model(X)
            _, predicted_labels = torch.max(y_prob, 1)

            n += y_true.size(0)
            correct_pred += (predicted_labels == y_true).sum()

    return correct_pred.float() / n


def training_loop(model: object, criterion: object, optimizer: object, train_loader: object, valid_loader: object,
                  epochs: int, device: str, print_every=1) -> (object, object, ([float], [float])):
    """
    Function defining the entire training loop
    """

    # set objects for storing metrics
    train_losses = []
    valid_losses = []

    # Train model
    for epoch in range(0, epochs):

        # training
        model, optimizer, train_loss = train(train_loader, model, criterion, optimizer, device)
        train_losses.append(train_loss)

        # validation
        with torch.no_grad():
            model, valid_loss = validate(valid_loader, model, criterion, device)
            valid_losses.append(valid_loss)

        if epoch % print_every == (print_every - 1):
            train_acc = get_accuracy(model, train_loader, device=device)
            valid_acc = get_accuracy(model, valid_loader, device=device)

            print(f'{datetime.now().time().replace(microsecond=0)} --- '
                  f'Epoch: {epoch}\t'
                  f'Train loss: {train_loss:.4f}\t'
                  f'Valid loss: {valid_loss:.4f}\t'
                  f'Train accuracy: {100 * train_acc:.2f}\t'
                  f'Valid accuracy: {100 * valid_acc:.2f}')

    return model, optimizer, (train_losses, valid_losses)


if __name__ == '__main__':
    train_loader, test_loader = loadData(TRAIN_DATA_PATH, TEST_DATA_PATH)
    device = detect_gpu()
    net = lenet.LeNet(NUMBER_OF_CLASSES).to(device)
    loss_fn = nn.CrossEntropyLoss()
    opt = optim.Adam(net.parameters(), lr=LEARNING_RATE)
    trainedModel, _, _ = training_loop(net, loss_fn, opt, train_loader, test_loader, N_EPOCHS, device)
    torch.save(trainedModel, PATH)
