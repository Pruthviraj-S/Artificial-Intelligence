import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# import data
data = pd.read_csv('../iris dataset/iris.csv')
print('Data: ',data)

print(data.shape)
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
data.columns = col_names

print('Info: ',data.info())

print('Counts: ',data['species'].value_counts())

target_col = ['species']
X = data.drop(['species'], axis=1)
y = data['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

# gini index
clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
clf_gini.fit(X_train, y_train)
y_pred_gini = clf_gini.predict(X_test)
print('Array: ',y_pred_gini)

print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred_gini)))
# y_pred_gini are the predicted class labels in the test-set.

print('Training set score: {:.4f}'.format(clf_gini.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(clf_gini.score(X_test, y_test)))
# plot
plt.figure(figsize=(12,8))
tree.plot_tree(clf_gini.fit(X_train, y_train))
plt.show()