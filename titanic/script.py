import numpy as np
import pandas as pd
from numpy import *
from math import e,log


def sigmoid(y):
	return 1.0 / (1.0 + np.exp(np.multiply(-1.0, y)))



df=pd.read_csv('train.csv',header=0)
'''
df.dtypes
df.info()
'''
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


target=target.reshape((len(data),1))
bias=np.ones(891)
bias=bias.reshape((len(data),1))

data=np.hstack((data,bias))

####ADD BIAS

o=np.array([[1],[0],[0],[0]])
o=o.reshape((4,1))

iterations=900
r=0.3
n=891



for j in range(iterations):


	h=dot(data,o)
	for i in range(len(h)):
		h[i]=1/(1+e**-(h[i]))

	o=o-(r*dot(data.transpose(),(h-target)))/n



'''

df			o		target

891 *4		4*1		891*1	

h=df*o
g=    1
  _________
       -h
   (1+e  )

o=o+r*(df')*(target-h)


'''


##PREPARING DATA
##########ALL AGES FILLED PREPARE FOR GLORY 


####

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
h=dot(df2,o)
fileObj=open('answer.csv','w')
for i in range(len(h)):
	h[i]=1/(1+e**-(h[i]))
	h[i]=np.around(h[i])
	fileObj.write(str(i+892)+str(',')+str(int(h[i]))+'\n')	