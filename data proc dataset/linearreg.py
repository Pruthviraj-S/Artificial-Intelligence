from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as mt

# import dataset
data = pd.read_csv('./data proc dataset/headbrain.csv')

# x=independent, y=dependent
x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values
print(data.shape)
print(data.head(20))
# coorelation coeff:- np.corrcoef(x,y)

# plot the dataset
mt.scatter(x,y, c='green',label='Data Points')
mt.xlabel('Head Size(cm^3)')
mt.ylabel('Brain Weight(grams)')
mt.legend()
mt.show()

# mean
mean_x = np.mean(x)
mean_y = np.mean(y)
n = len(x)

# theta1 & theta2
numerator = 0
denominator = 0
for i in range(n):
    numerator += (x[i]-mean_x)*(y[i]-mean_y)
    denominator += (x[i]-mean_x)**2
# slope(m)
b1 = numerator/denominator  
# coeff(c)
b0 = mean_y - (b1*mean_x)   
print('regression coeffs:',b1,b0)

# plot value and regression line
mt.rcParams['figure.figsize']=(10.0,5.0)
# max_x = np.max(x) + 100
# min_x = np.min(x) - 100
pred_y= b0 + (b1 * x)
# plot line
mt.plot(x,pred_y,color='yellow',label='Regression line')
# plot scatterpoints
mt.scatter(x,y,color='green',label='Scatter data')
mt.xlabel('Head Size in cm3')
mt.ylabel('Brain Weight in grams')
mt.legend()
mt.show()

# Calculating Root Mean Squares Error
rmse = 0
for i in range(n):
    y_pred = b0 + b1 * x[i]
    rmse += (y[i] - y_pred) ** 2
    
rmse = np.sqrt(rmse/n)
print("Root Mean Square Error is",rmse)

# Calculating R2 Score
ss_tot = 0
ss_res = 0
for i in range(n):
    y_pred = b0 + b1 * x[i]
    ss_tot += (y[i] - mean_y) ** 2
    ss_res += (y[i] - y_pred) ** 2
r2 = 1 - (ss_res/ss_tot)
print("R2 Score",r2)