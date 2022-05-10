import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# datatset 
train_data = pd.read_csv('./titanic dataset/train.csv')
print(train_data.head(5))
print('\nCount:\n',train_data.count())

print('\nCountplot: ',sb.countplot(x = 'Survived',hue = 'Pclass',data = train_data))
# AxesSubplot:xlabel = 'Survived',ylabel = 'count'

# Data Wrangling
def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train_data[train_data['Pclass'] == Pclass]['Age'].mean())
    else:
        return Age

train_data['Age'] = train_data[['Age','Pclass']].apply(add_age,axis = 1)
train_data.drop('Cabin',inplace = True,axis = 1)
train_data.dropna(inplace = True)

# # embarked
# embarked = pd.get_dummies(train_data['Embarked'],drop_first=True)
# embarked = pd.get_dummies(train_data['Pclass'],drop_first=True)
# train_data.drop(['PassengerId','Pclass','Name','Sex','Ticket','Embarked'],axis=1,inplace=True)

# x = train_data.drop('Survived',axis=1)
# y = train_data['Survived']

# # split for test train
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)

# # logistic regression 
# logmodel = LogisticRegression()
# logmodel.fit(x_train,y_train)
# LogisticRegression()

# # prediction 
# predictions = logmodel.predict(x_test)
# print('\npredictions:\n',classification_report(y_test, predictions))

# # confusion matrix 
# print('\nConfusion matrix:\n',confusion_matrix(y_test, predictions))

# Find survived passengers when Pclass=1 & gender=M
# method 1
# que1=train_data.loc[train_data['Survived']==1]
# que1=que1.loc[que1['Pclass']==1]
# que1=que1.loc[que1['Sex']=='male']
# print('\nNumber of survived passengers when  Pclass=1 & gender=M: ',que1['Survived'].count())
# method 2
que1_met2 = train_data[(train_data['Pclass']==1) & (train_data['Survived']==1) & (train_data['Sex']=='male')]
print('\nNumber of survived passengers when  Pclass = 1 & gender = M: ',que1_met2['Survived'].count())

# Find survived passengers when age>40 & sibsp=0
que2 = train_data[(train_data['Age']>40) & (train_data['Survived']==1) & (train_data['SibSp']==0)]
print('\nNumber of survived passengers when age > 40 & sibsp = 0: ',que2['Survived'].count())

# count number of family travelling together
que3 = train_data[(train_data['SibSp'])>0]
print('\nNumber of family travelling together: ',que3['Survived'].count())

# Find survived passengers when pclass=3,gender=F & age<12
que4 = train_data[(train_data['Pclass']==3) & (train_data['Survived']==1) & (train_data['Sex']=='female') & (train_data['Age']<12)]
print('\nNumber of survived passengers when pclass = 3,gender = F & age < 12: ',que4['Survived'].count())

# improve confusion matrix by paramtere re-engineering