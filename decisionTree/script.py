#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numpy import *
from math import e, log
from ete2 import Tree
data = pd.read_csv('data.csv', header=0)


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
            if data['Decision'][i] == 'p' and data[column][i] \
                == feature:
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

#########SEARCH BEGINS HERE
def search(t,testData):
    searchNode=t.get_tree_root()
    columnNames = list(data.columns.values)
    cnt=0
    while(cnt<len(columnNames)):
        cnt+=1
        key=''
        #print searchNode.name
        for child in searchNode.children:
            k=child.name.keys()
            #print child.name
            listOfKeys=searchNode.name.keys()
            for element in k:
                if(element not in listOfKeys):
                    key=element
                    break
    
        #print key
        #print searchNode.children        
        for child in searchNode.children:
            #print child.name[key]
            #print testData[key]
            if(child.name[key]==testData[key]):
                searchNode=child
                break        
       #print '______________________________'

    return searchNode



#########SEARCH ENDS HERE








columnNames = list(data.columns.values)
possibleValues = {}
for column in columnNames:

    for name in data[column]:
        if not possibleValues.has_key(column):
            possibleValues[column] = []
        else:
            xx = 55555

            # john snow

        if name in possibleValues[column]:
            yyyyy = 555
        else:
            possibleValues[column].append(name)

############CONSTRUCT TREE

columnUsed = columnNames

t = Tree()
root = t.get_tree_root()
root.name = {}
parents = [root]

while columnUsed:
    maxEntropy = 0
    maxChoice = -1

    for column in columnUsed:
        if 0.94 - findEntropy(data, column, possibleValues) \
            > maxEntropy and column != 'Decision':
            maxEntropy = 0.94 - findEntropy(data, column,
                    possibleValues)
            maxChoice = column
    if maxChoice in columnUsed:
        columnUsed.remove(maxChoice)

    print maxEntropy    
        
    children = []

    if maxChoice != -1:
        for parent in parents:
            cnt = 0
            for column in possibleValues[maxChoice]:
                parent.add_child()
            for column in possibleValues[maxChoice]:

                parent.children[cnt].name = {}
                for key in parent.name:
                    parent.children[cnt].name[key] = parent.name[key]

                parent.children[cnt].name[maxChoice] = column
                children.append(parent.children[cnt])
                cnt += 1
        parents = children
    else:

        break

    cnt = 0



#########CONSTRUCTED DECISION TREE TO DO IS SEARCH AND FIND APPROPRIATE CLASS USING ID3
testData={'Outlook':'rain','Temperature':'mild','Humidity':'normal','Windy':True}
columnNames = list(data.columns.values)
columnNames.remove('Decision')



searchNode=search(t,testData)
print searchNode
for i in range(len(data)):
    flag=True
    for key in testData.keys():
        if(data[key][i]!=searchNode.name[key]):
            flag=False
    if(flag==True):
        print i
        print data['Decision'][i]
        break                

