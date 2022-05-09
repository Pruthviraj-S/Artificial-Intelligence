import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split

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

# embarked
embarked = pd.get_dummies(train_data['Embarked'],drop_first=True)
embarked = pd.get_dummies(train_data['Pclass'],drop_first=True)
train_data.drop(['PassngerId','Pclass','Name','Sex','Ticket','Embarked'],axis=1,inplace=True)

x = train_data.drop('survived',axis=1)
y = train_data['Survived']