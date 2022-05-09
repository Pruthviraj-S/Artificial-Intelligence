import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# datatset 
train_data = pd.read_csv('./titanic dataset/train.csv')
print(train_data.head(20))
print('\nCount:\n',train_data.count())