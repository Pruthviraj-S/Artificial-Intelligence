# Write a python program for demonstrating use of pandas

import pandas as pd
# dataframe using pandas
df = pd.DataFrame({'Name': ['pvs', 'rushabh', 'het', 'Manan', 'dhruv', 'raj'], 'Salary': [
                  10000, 20000, 25000, 35000, 45000, 50000]})
print(df.head())

# calculate statistics
print('\nMin :' + str(df['Salary'].min()))
print('\nMax :' + str(df['Salary'].max()))
print('\nMean :' + str(df['Salary'].mean()))
print('\nMedian :' + str(df['Salary'].median()))
print('\nMod :' + str(df['Salary'].mode()))

df['Salary'].describe()