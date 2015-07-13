import numpy as np 
import pandas as pd
from numpy import *
from math import e, log
data = pd.read_csv('data.csv', header=0)

class DecisionTree:
	def __init__(self):
		self.constraints={}
		self.isLeaf=False
		self.decision=''
		self.children=[]
		self.entropy=0

def populate(data,columnNames):
		possibleValues = {}
		for column in columnNames:
		    for name in data[column]:
		        if not possibleValues.has_key(column):
		            possibleValues[column] = []
		        
		        if name not in possibleValues[column]:
		            possibleValues[column].append(name)

		return possibleValues           

def findEntropy(data, column, possibleValues):
    pFeature = {}
    for feature in possibleValues[column]:
        cnt = 0
        for row in data[column]:
            if row == feature:
                cnt = cnt + 1
        pFeature[feature] = float(cnt) / len(data)

    entropy = 0
    
    for feature in pFeature.keys():
        entropyChild = 0
        pcnt = 0
        cnt = 0

        for i in range(len(data)):
            if data[column][i] == feature:
                cnt = cnt + 1
            if data['Decision'][i] == 'p' and data[column][i] == feature:
                pcnt += 1
        

        pcnt = float(pcnt) / cnt
        ncnt = 1 - pcnt
    

        if pcnt != 0 and ncnt != 0:
            entropyChild = -(pcnt * log(pcnt, 2)) - ncnt * log(ncnt, 2)
        elif pcnt == 0:
            entropyChild = -(ncnt * log(ncnt, 2))
        elif ncnt == 0:
            entropyChild = -(pcnt * log(pcnt, 2))

        entropy -= -pFeature[feature] * entropyChild
   		
    return entropy




def build(tree,data):
		columnNames = list(data.columns.values)
	
		possibleValues=populate(data,columnNames)
	
		findEntropy(data,'Decision',possibleValues)
		
		
		columnNames.remove('Decision')
		possibleValues.pop('Decision')
		
		while columnNames:
			maxEntropy=0
			removed=-1
			for column in columnNames:
				if(0.94-findEntropy(data,column,possibleValues) > maxEntropy):
					maxEntropy=0.94-findEntropy(data,column,possibleValues) 
					removed=column
			print removed
			columnNames.remove(removed)			 
			
		



		
tree=DecisionTree()

build(tree,data)