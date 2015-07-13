import numpy as np 
import pandas as pd 
import csv
from pandas import *
from  sklearn import *
from  featuretransform import *
from validator import validate

def readFromCSV(filename):
	data = []
	with open(filename,"rb") as file:
		reader = csv.reader(file,delimiter=',')
		[data.append(row) for row in reader ]
	return data



data = readFromCSV("train.csv")
columns = data[0]
data = DataFrame(data[1:10000])
data.columns = columns
print data.columns



### FEATURE TRANSFORMATION STEPS
data['DayOfWeek'] = convertStringToIntMap(data["DayOfWeek"])
data['Category'] = convertStringToIntMap(data["Category"],True)
data['PdDistrict'] = convertStringToIntMap(data['PdDistrict'])
data['Resolution'] = convertStringToIntMap(data['Resolution'])
data['Dates'] = dateTransformer(data['Dates'])



data = data.drop('Address', 1)
data = data.drop('Descript', 1)
data = data.drop('PdDistrict', 1)

target = data['Category']
data = data.drop('Category', 1)

data = np.array(data)
target = np.array(target)

lr = linear_model.LogisticRegression()
lr.fit(data,target)

categoryMap = {'KIDNAPPING': 0, 'WEAPON LAWS': 1, 'SECONDARY CODES': 2, 'WARRANTS': 3, 'PROSTITUTION': 4, 'DRIVING UNDER THE INFLUENCE': 5, 'SEX OFFENSES FORCIBLE': 6, 'ROBBERY': 7, 'BURGLARY': 8, 'SUSPICIOUS OCC': 9, 'FAMILY OFFENSES': 10, 'FORGERY/COUNTERFEITING': 11, 'DRUNKENNESS': 12, 'OTHER OFFENSES': 13, 'FRAUD': 14, 'ARSON': 15, 'DRUG/NARCOTIC': 16, 'TRESPASS': 17, 'LARCENY/THEFT': 18, 'VANDALISM': 19, 'NON-CRIMINAL': 20, 'VEHICLE THEFT': 21, 'STOLEN PROPERTY': 22, 'ASSAULT': 23, 'MISSING PERSON': 24, 'DISORDERLY CONDUCT': 25, 'RUNAWAY': 26}
categoryArray = "ARSON,ASSAULT,BAD CHECKS,BRIBERY,BURGLARY,DISORDERLY CONDUCT,DRIVING UNDER THE INFLUENCE,DRUG/NARCOTIC,DRUNKENNESS,EMBEZZLEMENT,EXTORTION,FAMILY OFFENSES,FORGERY/COUNTERFEITING,FRAUD,GAMBLING,KIDNAPPING,LARCENY/THEFT,LIQUOR LAWS,LOITERING,MISSING PERSON,NON-CRIMINAL,OTHER OFFENSES,PORNOGRAPHY/OBSCENE MAT,PROSTITUTION,RECOVERED VEHICLE,ROBBERY,RUNAWAY,SECONDARY CODES,SEX OFFENSES FORCIBLE,SEX OFFENSES NON FORCIBLE,STOLEN PROPERTY,SUICIDE,SUSPICIOUS OCC,TREA,TRESPASS,VANDALISM,VEHICLE THEFT,WARRANTS,WEAPON LAWS".split(",")

print validate(lr,data,target)

print 'writing data'

testData = readFromCSV("test.csv")
columns = testData[0]
testData = DataFrame(testData[1:])
testData.columns = columns
testData['DayOfWeek'] = convertStringToIntMap(testData["DayOfWeek"])
testData['PdDistrict'] = convertStringToIntMap(testData['PdDistrict'])
testData['Dates'] = dateTransformer(testData['Dates'])
testData['X'] = numberTransformer(testData['X'])
testData['Y'] = numberTransformer(testData['Y'])



testData = testData.drop('Address', 1)
testData = testData.drop('Id', 1)

testData = np.array(testData)


cnt = 0
with open('answer.csv',"w") as file:
	for row in testData:
		answer = int(lr.predict(row))
		crimeCategory = categoryMap.keys()[categoryMap.values().index(answer)]
		answerVector = [0 for i in range(len(categoryArray))]
		answerVector[categoryArray.index(crimeCategory)] = 1
		file.write(str(cnt)+',')
		for i in answerVector:
			file.write(str(i)+',')
		file.write('\n')	
		cnt += 1




	

