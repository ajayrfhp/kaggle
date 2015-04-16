import numpy as np
import pandas as pd
from numpy import *
from math import e,log


def sigmoid(y):
	return 1.0 / (1.0 + np.exp(np.multiply(-1.0, y)))





df=pd.read_csv('train.csv',header=0)
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df[df['Age'].isnull()][['Sex','Pclass','Age']]

for i in range(len(df)):
	if(df.Age.isnull()[i]):
		df.Age[i]=29

target=df['Survived']
df = df.drop(['PassengerId','Survived','Sex','Name','SibSp','Parch','Ticket','Fare','Cabin','Embarked'], axis=1) 		


data=np.array(df)
target=np.array(target)


######################CLEANING DATA



n=data.shape[0]
m=data.shape[1]+1
iterations=50000
learningRate=0.15


target=target.reshape((n,1))

bias=np.ones(n)
bias=bias.reshape((n,1))
data=np.hstack((data,bias))

weights=np.zeros(m)
weights=weights.reshape((m,1))

for i in range(iterations):
	h=sigmoid(dot(data,weights))
	delta=dot(data.transpose(),(h-target))
	weights=weights-(learningRate*delta)/n

h=sigmoid(dot(data,weights))
print np.around(h)




df2=pd.read_csv('test.csv',header=0)
df2['Gender'] = df2['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
df2[df2['Age'].isnull()][['Sex','Pclass','Age']]

for i in range(len(df2)):
	if(df2.Age.isnull()[i]):
		df2.Age[i]=29

df2 = df2.drop(['PassengerId','Sex','Name','SibSp','Parch','Ticket','Fare','Cabin','Embarked'], axis=1) 		

bias=np.ones(len(df2))
bias=bias.reshape((len(df2),1))

df2=np.hstack((df2,bias))
h=np.around(sigmoid(dot(df2,weights)))
fileObj=open('answer.csv','w')
for i in range(len(h)):
	fileObj.write(str(892+i)+','+str(int(h[i]))+'\n')	




