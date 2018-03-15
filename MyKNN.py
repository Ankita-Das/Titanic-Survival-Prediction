##My K-Nearest Neighbor Classifier
import pandas as pd
from math import *
import csv
def MyKNN(K,a):
    print('Entering')
    Distance=[]
    train=pd.read_csv('/home/ankita/Desktop/Python files/Titanic/train.csv');
    test=pd.read_csv('/home/ankita/Desktop/Python files/Titanic/test.csv')
    
    #csv_train=csv.reader(train)
    #csv_test=csv.reader(test)
    for i,rowi in test.iloc[a-1:a].iterrows():
        print(rowi['PassengerId'])
        for j,rowj in train.iloc[:].iterrows():
            class_diff_sq=abs(rowi['Pclass']-rowj['Pclass'])**2
            sibsp_diff_sq=abs(rowi['SibSp']-rowj['SibSp'])**2
            age_diff_sq=abs(rowi['Age']-rowj['Age'])**2
            if rowi['Sex']==rowj['Sex']:
                sex_diff=0
            else:
                sex_diff=1
            
            sum2=list([sqrt(class_diff_sq+sibsp_diff_sq+age_diff_sq+sex_diff)])
            Distance=Distance+[sum2]

        break
    #print(Distance)
    #print(len(Distance))
    csv_f=open('/home/ankita/Desktop/Python files/Titanic/train_new.csv','w')
    csv_wr=csv.writer(csv_f)
    csv_rd=csv.reader(open('/home/ankita/Desktop/Python files/Titanic/train.csv'));
    i=0
    for row in csv_rd:
        #print(row)
        if i>0:
          csv_wr.writerow(row+[Distance[i-1][0]])
          #print(row+[Distance[i-1][0]])
        else:
          csv_wr.writerow(row+['Distance'])
          #print(row+['Distance'])
        i=i+1
    csv_f.close()
    countY=countN=0
    sort_train_new=pd.read_csv('/home/ankita/Desktop/Python files/Titanic/train_new.csv')
    sort_save=sort_train_new.sort_values('Distance')
    for k,rowk in sort_save.iloc[:K].iterrows():
        print(rowk['Survived'])
        if(rowk['Survived']==1):
            countY=countY+1
        else:
            countN=countN+1
    if countY>=countN:
        print('Survived')
    else:
        print('Dead')
    
    
K=int(input("No. of nearest neighbours to be considered:"))
a=int(input("Customer whose survival is to be predicted:"))
MyKNN(K,a)
            
            
        
        
