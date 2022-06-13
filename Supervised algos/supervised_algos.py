# Import pre-reqs
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score # to do
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
dataset.hist()
plt.show()