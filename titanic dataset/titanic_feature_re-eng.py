# lib imports
import numpy as np
import pandas as pd

# import data
train_data = pd.read_csv('./titanic dataset/train.csv',index_col='PassengerId')
test_data = pd.read_csv('./titanic dataset/test.csv',index_col='PassengerId')
survived = train_data['Survived'].copy()
train_data = train_data.drop('Survived',axis=1)

# check dimensions
print('\nTrain data: ',train_data.shape)
print('\nTest data: ',test_data.shape)

# merge both sets for feature re-eng
main_dataset = pd.concat([test_data,train_data])  
# get indexes
train_index = train_data.index        
test_index = test_data.index
