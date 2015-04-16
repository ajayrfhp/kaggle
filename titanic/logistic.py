import numpy as np
import pandas as pd
from numpy import *
from math import e,log


def sigmoid(y):
	return 1.0 / (1.0 + np.exp(np.multiply(-1.0, y)))



######################CLEANING DATA

data=np.array([[0, 0], [0, 1], [1, 0], [1, 1]])


n=data.shape[0]
m=data.shape[1]+1
iterations=5000
learningRate=0.15

target=np.array([0, 0, 0, 1])
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
	cost=-(target.transpose()*np.log(h))-((1-target.transpose())*(1-np.log(h)))
	print (sum(sum(cost))/n)
h=sigmoid(dot(data,weights))
print np.log(h)




