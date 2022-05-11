#mtcs_45
import numpy as np
import pandas as pd


#import dataset
dataset = pd.read_csv('./Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
print('\nimport dataset:')
print(x)
print(y)

# #dataclean
# from sklearn.impute import *
# imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# imputer.fit(x[:,1:3])
# x[:,1:3] = imputer.transform(x[:,1:3])
# print('\nclean data:')
# print(x)

# #encoding categorical data
# from sklearn.preprocessing import LabelEncoder
# lex = LabelEncoder()
# x[:,0] = lex.fit_transform(x[:,0])
# print('\ncategorical data:')
# print(x)

# #encoding independent variable
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
# x = np.array(ct.fit_transform(x))
# print('\nindependent variable:')
# print(x)

# #encoding dependent variable
# le = LabelEncoder()
# y = le.fit_transform(y)
# print('\ndependent variable:')
# print(y)

# #splitting the dataset into the training set and test set
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
# print('\nsplitting the dataset into the training set and test set:')
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# #feature scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# x_train[:,3:] = sc.fit_transform(x_train[:,3:])
# x_test[:,3:] = sc.transform(x_test[:,3:])
# print('\nfeature scaling:')
# print(x_train)
# print(x_test)