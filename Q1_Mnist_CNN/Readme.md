## Q1 : MNIST-CNN

### Goal
1. Build a multi-class classifier
2. Library should be trainable on other dataset


### Installation
To install required dependencies, follow these steps:

Linux and macOS:
```
$ pip install -r requirements.txt
```


### Using MNIST_CNN

#### Directory Structure : Mnist_CNN
 * [code](./code) : Contrains all code associated with repo
   * [dataloader.py](./code/dataloader.py) : Reads data stored in `../data`
   * [lenet.py](./code/lenet.py) : Model architecture for Lenet CNN
   * [train.py](./code/train.py) : Train lenet on data loaded from dataloader
   * [infer.py](./code/infer.py) : Loads trained model and infers on new input 
    
 
* [data](./data) : FMNIST data is placed here
  * [f_mnist_data](./data/f_mnist_data) : Place MNIST data set here
    *  [test](./data/f_mnist_data/test) : Place test data here. Each sub-directory in this directory contains images associated with a particular label
    *  [train](./data/f_mnist_data/train) : Place train data here. Each sub-directory in this directory contains images associated with a particular label


* [models](./models) : Saved models are placed in this directory

#### Train and Infer
To update the data the model is trained on, please change the following variables in `train.py`:\
`TRAIN_DATA_PATH` : Directory containing training data \
`TEST_DATA_PATH` : Directory containing test data


To train and infer follow these steps:

Trainstep : `python3 train.py` \
Inferstep : `python3 infer.py`

### Dataset Used:
Link : https://github.com/DeepLenin/fashion-mnist_png

**MNIST Fashion** \
Train Set : 60,000 \
Test Set : 10,000 \
Classes : 10



**Helper Docs**

https://towardsdatascience.com/understanding-and-implementing-lenet-5-cnn-architecture-deep-learning-a2d531ebc342