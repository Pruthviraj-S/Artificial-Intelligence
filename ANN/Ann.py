#install required libraries
#data visualization packages
import matplotlib.pyplot as plt
import random 
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()
print ("X_train shape", X_train.shape)
print ("y_train shape", y_train.shape)
print ("X_test shape", X_test.shape)
print ("y_test shape", y_test.shape)

plt.rcParams['figure.figsize'] = (9,9)
for i in range (9):
    plt.subplot(3,3,i+1)
    num = random.randint (0, len(X_train))
    plt.imshow(X_train[num], cmap='gray', interpolation = 'none')
    plt.title("Class {}".format(y_train[num]))

plt.tight_layout()
plt.show()