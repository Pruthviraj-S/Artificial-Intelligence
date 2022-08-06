# Write a python program for demonstrating use of Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame ({'Name' : ['Anubhav', 'Reyansh', 'Shruti', 'Sanaya'], 'Salary': [10000, 200000, 2500, 35000]})
salary = df['Salary']
# data plotting
salary.plot.hist(title = 'Salary Distribution', color ='grey', bins=25)
plt.axvline(salary.mean(), color ='blue', linestyle = 'dashed', linewidth = 2)
plt.axvline(salary.median(), color ='red', linestyle = 'dashed', linewidth = 2)
plt.show()