import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'Name':['a','b','c','d'],'Salary':[10000,22000,35000,40000]})
print(df.head())

#calculate Statistics
print('Min:' +str (df['Salary'].min()))
print('Max:' +str (df['Salary'].max()))
print('Mean:' +str (df['Salary'].mean()))
print('Median:' +str (df['Salary'].median()))
print('Mode:\n' +str (df['Salary'].mode()))

print(df['Salary'].describe())
print(df['Salary'].describe()['count'])

#%matplotlib inline
salary = df['Salary']
salary.plot.hist(title = 'Salary Distribution', color='yellow', bins=25)
plt.axvline(salary.mean(),color='blue',linestyle='dashed',linewidth=2)
plt.axvline(salary.median(),color='red',linestyle='dashed',linewidth=2)
plt.show() 