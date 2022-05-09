import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./iris dataset/iris.csv')
print('\nFirst 5 Entries:',df.head())
print('\nLast 5 Entries:',df.tail())

#calculate Statistics
print(df.describe())

#plot sepal_length
sepal_length = df['sepal_length']
sepal_length.plot.hist(title = 'sepal_length', color='yellow', bins=25)
plt.axvline(sepal_length.mean(),color='blue',linestyle='dashed',linewidth=2)
plt.show()
#plot sepal_width
sepal_width = df['sepal_width']
sepal_width.plot.hist(title = 'sepal_width',color='orange', bins=25)
plt.axvline(sepal_width.mean(),color='purple',linestyle='dashed',linewidth=2)
plt.show()
#plot petal_length
petal_length = df['petal_length']
petal_length.plot.hist(title = 'petal_length',color='green', bins=25)
plt.axvline(petal_length.mean(),color='grey',linestyle='dashed',linewidth=2)
plt.show()
#plot petal_width
petal_width = df['petal_width']
petal_width.plot.hist(title = 'petal_width',color='red', bins=25)
plt.axvline(petal_width.mean(),color='black',linestyle='dashed',linewidth=2)
plt.show()