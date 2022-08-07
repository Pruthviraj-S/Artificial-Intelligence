# Naive Bayes
import pandas
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv('../iris dataset/iris.csv', names=names)

print('Head: \n',dataset.head(3))

array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 6
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=validation_size, random_state=seed)

seed = 6
scoring = 'accuracy'

models = []
models.append(('NB', GaussianNB()))
results = []
cv_results = model_selection.cross_val_score(
    GaussianNB(), X_train, Y_train, scoring=scoring)
results.append(cv_results)
value = "%f" % (cv_results.mean())
print('Value: ',value)
