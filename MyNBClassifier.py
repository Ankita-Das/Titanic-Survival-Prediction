import pandas as pd
train=pd.read_csv('/home/ankita/Desktop/Python files/Titanic/train.csv')
test=pd.read_csv('/home/ankita/Desktop/Python files/Titanic/test.csv')

#Comparing Columns with #survived #male or #female

P_male_yes=0
P_fem_yes=0
P_male_no=0
P_fem_no=0
for i,rowi in train.iloc[:].iterrows():
    if rowi['Survived']==1 and rowi['Sex']=='male':
        P_male_yes=P_male_yes+1
    elif rowi['Survived']==1 and rowi['Sex']=='female':
        P_fem_yes=P_fem_yes+1
    elif rowi['Survived']==0 and rowi['Sex']=='male':
        P_male_no=P_male_no+1
    elif rowi['Survived']==0 and rowi['Sex']=='female':
        P_fem_no=P_fem_no+1
    else:
        print(rowi['Sex'])
P_sex_yes=P_male_yes+P_fem_yes
P_male_yes=P_male_yes/P_sex_yes
P_fem_yes=P_fem_yes/P_sex_yes

P_sex_no=P_male_no+P_fem_no
P_male_no=P_male_no/P_sex_no
P_fem_no=P_fem_no/P_sex_no

print("No of female survived:"+str(P_fem_yes))
print('No of female dead:'+str(P_fem_no))
print("No of male survived:"+str(P_male_yes))
print("No of male dead:"+str(P_male_no))

#Pclass wise
P_class1_yes=0
P_class1_no=0
P_class2_yes=0
P_class2_no=0
P_class3_yes=0
P_class3_no=0
for i,rowi in train.iloc[:].iterrows():
    if rowi['Survived']==1 and rowi['Pclass']==1:
        P_class1_yes=P_class1_yes+1
    elif rowi['Survived']==1 and rowi['Pclass']==2:
        P_class2_yes=P_class2_yes+1
    elif rowi['Survived']==1 and rowi['Pclass']==3:
        P_class3_no=P_class3_no+1
    elif rowi['Survived']==0 and rowi['Pclass']==1:
        P_class1_no=P_class1_no+1
    elif rowi['Survived']==0 and rowi['Pclass']==2:
        P_class2_no=P_class2_no+1
    elif rowi['Survived']==0 and rowi['Pclass']==3:
        P_class3_no=P_class3_no+1
    else:
        print(rowi['Pclass'])
P_class_yes=P_class1_yes+P_class2_yes+P_class3_yes
P_class1_yes=P_class1_yes/P_class_yes
P_class2_yes=P_class2_yes/P_class_yes
P_class3_yes=P_class3_yes/P_class_yes

P_class_no=P_class1_no+P_class2_no+P_class3_no
P_class1_no=P_class1_no/P_class_no
P_class2_no=P_class2_no/P_class_no
P_class3_no=P_class3_no/P_class_no



print("No of class1 survived:"+str(P_class1_yes))
print('No of class1 dead:'+str(P_class1_no))
print("No of class2 survived:"+str(P_class2_yes))
print("No of class2 dead:"+str(P_class2_no))

#Embarking wise
P_S_yes=0
P_S_no=0
P_C_yes=0
P_C_no=0
P_Q_yes=0
P_Q_no=0

for i,rowi in train.iloc[:].iterrows():
    if rowi['Survived']==1 and rowi['Embarked']=='S':
        P_S_yes=P_S_yes+1
    elif rowi['Survived']==1 and rowi['Embarked']=='C':
        P_C_yes=P_C_yes+1
    elif rowi['Survived']==1 and rowi['Embarked']=='Q':
        P_Q_no=P_Q_no+1
    elif rowi['Survived']==0 and rowi['Embarked']=='S':
        P_S_no=P_S_no+1
    elif rowi['Survived']==0 and rowi['Embarked']=='C':
        P_C_no=P_C_no+1
    elif rowi['Survived']==0 and rowi['Embarked']=='Q':
        P_Q_no=P_Q_no+1
    else:
        print(rowi['Embarked'])

P_emb_yes=P_S_yes+P_C_yes+P_Q_yes
P_S_yes=P_S_yes/P_emb_yes
P_C_yes=P_C_yes/P_emb_yes
P_Q_yes=P_Q_yes/P_emb_yes

P_emb_no=P_S_no+P_C_no+P_Q_no
P_S_no=P_S_no/P_emb_no
P_C_no=P_C_no/P_emb_no
P_Q_no=P_Q_no/P_emb_no
prod_yes=100
prod_no=100
for j,rowj in test.iloc[16:17].iterrows():
    print(rowj['PassengerId'])
    if rowj['Sex']=='male':
        prod_yes=prod_yes*P_male_yes
        print("Survived male:"+str(prod_yes))
        prod_no=prod_no*P_male_no
        print("Dead male:"+str(prod_no))
    elif rowj['Sex']=='female':
        prod_yes=prod_yes*P_fem_yes
        print("Survived female:"+str(prod_yes))
        prod_no=prod_no*P_fem_no
        print("DEad female:"+str(prod_no))

    if rowj['Embarked']=='S':
        prod_yes=prod_yes*P_S_yes
        print("Survived emb S"+str(prod_yes))
        prod_no=prod_no*P_S_no
        print("DEad emb S"+str(prod_no))
    elif rowj['Embarked']=='C':
        prod_yes=prod_yes*P_C_yes
        print("Survived emb C"+str(prod_yes))
        prod_no=prod_no*P_C_no
        print("DEad emb C"+str(prod_no))
    elif rowj['Embarked']=='Q':
        prod_yes=prod_yes*P_Q_yes
        print("Survived emb Q:"+str(prod_yes))
        prod_no=prod_no*P_Q_no
        print("Dead emb Q:"+str(prod_no))


    if rowj['Pclass']==1:
        prod_yes=prod_yes*P_class1_yes
        print('Survived class 1:'+str(prod_yes))
        prod_no=prod_no*P_class1_no
        print('Dead class 1:'+str(prod_no))
    elif rowj['Pclass']==2:
        prod_yes=prod_yes*P_class2_yes
        print('Survived class 2:'+str(prod_yes))
        prod_no=prod_no*P_class2_no
        print('DEad class 2:'+str(prod_no))
    elif rowj['Pclass']==3:
        prod_yes=prod_yes*P_class3_yes
        print('Survived class 3:'+str(prod_yes))
        prod_no=prod_no*P_class3_no
        print('DEad class 3:'+str(prod_no))
print('true prod yes:'+str(prod_yes))
print('true prod no:'+str(prod_no))
P_sur_yes=prod_yes/(prod_yes+prod_no)
P_sur_no=prod_no/(prod_yes+prod_no)
if(P_sur_yes>P_sur_no):
    print('Survived with probablility'+str(P_sur_yes))
else:
    print('Died with probability'+str(P_sur_no))

        
            
                

        

