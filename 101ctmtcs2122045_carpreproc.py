#mtcs_45, 101ctmtcs2122045
import numpy as np
import pandas as pd
from sklearn.impute import *
from sklearn.preprocessing import LabelEncoder
#from sklearn.compose import ColumnTransformer
#from sklearn.preprocessing import OneHotEncoder

#import dataset
data = pd.read_csv('./data proc dataset/car_ad.csv',encoding='iso-8859-9')

#dataclean
print(data.isnull().sum())
#remove rows with missing values since drive is not numerical
data= data.dropna(subset=['drive'])

#replace nan with mean for engV
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(data[['engV']])
data[['engV']] = imputer.transform(data[['engV']])

#replace 0 with mean for price & mileage
imputer = SimpleImputer(missing_values=0, strategy='mean')
imputer.fit(data[['price']])
data[['price']] = imputer.transform(data[['price']])
imputer.fit(data[['mileage']])
data[['mileage']] = imputer.transform(data[['mileage']])

print('\nclean data:')
print(data.head(20))
print(data.describe(include='all'))

#encoding categorical data
lex = LabelEncoder()
data['car'] = lex.fit_transform(data['car'])
data['body'] = lex.fit_transform(data['body'])
data['engType'] = lex.fit_transform(data['engType'])
data['registration'] = lex.fit_transform(data['registration'])
data['model'] = lex.fit_transform(data['model'])
print('\ncategorical data:')
print(data.head(20))

x = data[['car','body','mileage','engV','engType','registration','year','model','drive']]
y = data[['price']]
print('\nx:')
print(x)
print('\ny:')
print(y)

# #encoding independent variable
# ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
# x = np.array(ct.fit_transform(x))
# print('\nindependent variable:')
# print(x)

# #encoding dependent variable
# le = LabelEncoder()
# y = le.fit_transform(y)
# print('\ndependent variable:')
# print(y)

#splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
print('\nsplitting the dataset into the training set and test set:')
print(x_train)
print(x_test)
print(y_train)
print(y_test)