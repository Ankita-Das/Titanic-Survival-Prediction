from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier

from sklearn.preprocessing import Imputer,Normalizer,scale
from sklearn.cross_validation import train_test_split,StratifiedKFold

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns

import numpy as np
import pandas as pd

train=pd.read_csv('train.csv');
test=pd.read_csv('test.csv')

full=train.append(test,ignore_index=True)
titanic=full[:891]

del train,test
print('Datasets:','full',full.shape,'titanic:',titanic.shape)

print(titanic.head())
print(titanic.describe())

sex=pd.Series(np.where(full['Sex']=='male',1,0),name='Sex')
embarked=pd.get_dummies(full.Embarked,prefix='Embarked')
print(embarked.head())
pclass=pd.get_dummies(full.Pclass,prefix='Pclass')
print(pclass.head())

#fill in the missing values
imputed=pd.DataFrame()
imputed['Age']=full.Age.fillna(full.Age.mean())
imputed['Fare']=full.Fare.fillna(full.Fare.mean())
print(imputed.head())

title=pd.DataFrame()
title['Title']=full['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
title=pd.get_dummies(title.Title)
print(title.head())


def cleanticket(ticket):
    ticket=ticket.replace('.','')
    ticket=ticket.replace('/','')
    # print('before')
    #print(ticket)
    ticket=ticket.split()
    #print('after')
    #print(ticket)
    ticket=map(lambda t:t.strip(),ticket)
    ticket=list(filter(lambda t:not t.isdigit(),ticket))
    if len(ticket)>0:
        return ticket[0]
    else:
        return 'xxx'
ticket=pd.DataFrame()
ticket['Ticket']=full['Ticket'].map(cleanticket)
ticket=pd.get_dummies(ticket['Ticket'],prefix='Ticket')
print(ticket.shape)
print(ticket.head())

cabin=pd.DataFrame()
cabin['Cabin']=full.Cabin.fillna('U')
cabin['Cabin'].map(lambda c:c[0])
cabin=pd.get_dummies(cabin['Cabin'],prefix='Cabin')
print(cabin.head())



family=pd.DataFrame()
family['FamilySize']=full['Parch']+full['SibSp']+1

family['Family_Single']=family['FamilySize'].map(lambda s:1 if s==1 else 0)
family['Family_Small']=family['FamilySize'].map(lambda s:1 if 2<=s<=4 else 0)
family['Family_Large']=family['FamilySize'].map(lambda s:1 if 5<=s else 0)
print(family.head())


#assembling datasets
print('Assembled Data')
full_x=pd.concat([imputed,embarked,cabin,sex],axis=1)
print(full_x.head())

train_valid_x=full_x[0:891]
train_valid_y=titanic.Survived
test_x=full_x[891:]
train_x,valid_x,train_y,valid_y=train_test_split(train_valid_x,train_valid_y,train_size=.7)
print(full_x.shape,train_x.shape,valid_x.shape,train_y.shape,valid_y.shape,test_x.shape)

#model=RandomForestClassifier(n_estimators=100)
#model=SVC()
model=KNeighborsClassifier(n_neighbors=3)

#model=LogisticRegression()
model.fit(train_x,train_y)
print(model.score(train_x,train_y),model.score(valid_x,valid_y))


test_y=model.predict(test_x)
passenger_id=full[891:].PassengerId
test=pd.DataFrame({'PassengerId':passenger_id,'Survived':test_y})
print(test.shape)
print(test.head())
test.to_csv('titanic_pred.csv',index=False)

