# Import pre-reqs
import pandas as pd
import seaborn as sb
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# import dataset
dataset = pd.read_csv('../iris dataset/iris.csv')

# Shape dataset
print('\n(Rows,Columns): ',dataset.shape)

# First 10 Entries
print('\nFirst 10 Entries:\n',dataset.head(10))

# Describe dataset
print('\nDescribe dataset:\n',dataset.describe())

# group data and check for size
print('\nGroup:',dataset.groupby('species').size())

# box plot
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
plt.show()

# plot histogram
dataset.hist(color='pink')
plt.show()

# scatter matrix
scatter_matrix(dataset)
plt.show()

# Heatmap
heatplot=sb.heatmap(dataset.corr(),cmap='YlGnBu',annot=True)
plt.show()

# split data, train & test
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size=0.20
seed = 6
scoring = 'accuracy'
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=validation_size, random_state = seed)

# models
models = []
models.append (('LR', LogisticRegression()))
models.append (('LDA', LinearDiscriminantAnalysis()))
models.append (('KNN', KNeighborsClassifier()))
models.append (('CART', DecisionTreeClassifier()))
models.append (('NB', GaussianNB()))
models.append (('SVM', SVC()))

results = []
names = []

# crosss validation, data is split into parts of 10.
for name, model in models:
    kfold = model_selection.KFold(n_splits = 10)
    cv_results=model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring= 'accuracy')
    results.append(cv_results)
    names.append(name)
    print("%s:  %f  (%f)" % (name, cv_results.mean(), cv_results.std()))

# comparision of algos
fig =plt.figure()
fig.suptitle('Algorithm Comparision')
ax= fig.add_subplot(111)
plt.boxplot(results)
ax. set_xticklabels(names)
plt.show()