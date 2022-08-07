# Support vector machine
import pandas
from sklearn.svm import SVC
from sklearn import model_selection

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv('../iris dataset/iris.csv', names=names)

print('Head: \n', dataset.head(5))
print('Describe: \n', dataset.describe())
print(dataset.groupby('class').size())

# array
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 6
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=validation_size, random_state=seed)

seed = 6
scoring = 'accuracy'

# model ; svm
models = []
models.append(('SVM', SVC()))

results = []
kfold = model_selection.KFold(n_splits=10)
cv_results = model_selection.cross_val_score(
    SVC(), X_train, Y_train, cv=kfold, scoring=scoring)
results.append(cv_results)
value = "%f" % (cv_results.mean())
print('\nValue: ', value)
