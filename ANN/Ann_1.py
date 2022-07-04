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
plt.show()
#It will show the 3rd training image as python indexing starts with 0.
#perform data normalization so that all input values are between 0 and 1. 
#Since a grayscale image has pixel values of 0 to 255, we divide each pixel by 255. 
#Data normalization is necessary to reduce data redundancy and improve data integrity. 
#It makes sure your data is the same throughout your project.

# greyscale image : 00-FF, which is 0 to 255.
x_train_norm = x_train_full/255.
x_test_norm = x_test/255.

# split data into validation and training set
x_valid, x_train = x_train_norm[:5000], x_train_norm[5000:]
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

x_test = x_test_norm
#Training data are fed after each training in an epoch. 
#An epoch is when the entire training dataset passes through the neural network once. 

np.random.seed(42)
tf.random.set_seed(42)
#42 is used as random seed in ML

# Create keras model
model = keras.models.Sequential()

model.add(keras.layers.Flatten(input_shape=[28,28])) # 1 flatten layer as the input layer
model.add(keras.layers.Dense(300, activation="relu")) # 2 dense relu layers as hidden layers 
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax")) # a dense softmax layer as the output layer
#A flattening layer flattens the input to a single-column array. It prepares the input data for the next dense layers. 
#a dense layer is a layer of parallel perceptrons.

# relu is used on hidden layers
#sigmoid and softmax are used for output. 
#Softmax is often used as the activation for the last layer of a classification network because the result could be interpreted as a probability distribution.