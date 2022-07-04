# ann 
# imports
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# keras - an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library. Up until version 2.3, Keras supported multiple backends, including TensorFlow, Microsoft Cognitive Toolkit, Theano, and PlaidML
mnist = keras.datasets.mnist
(x_train_full, y_train_full),(x_test, y_test) = mnist.load_data()
#The dataset is structured as a tuple of NumPy arrays: x training images, y training labels, and x test images, y test labels.
# Downloads data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

plt.imshow(x_train_full[2])
#It will show the 3rd training image as python indexing starts with 0.
#perform data normalization so that all input values are between 0 and 1. 
#Since a grayscale image has pixel values of 0 to 255, we divide each pixel by 255. 
#Data normalization is necessary to reduce data redundancy and improve data integrity. 
#It makes sure your data is the same throughout your project.