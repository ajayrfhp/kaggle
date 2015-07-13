def convertStringToIntMap(column,isCategory=False):
	categoryMap = {}
	columnList = list(set(column))
	for i in range(len(column)):
		if(isCategory):
			categoryMap[column[i]] = columnList.index(column[i])
		column[i] = columnList.index(column[i])
	if(isCategory):
		print categoryMap

	return column
		

def dateTransformer(column):
	for i  in range(len(column)):
		date = column[i].split(' ')[0].split('-')
		year = date[0]
		month = int(date[1])
		day = int(date[2])
		dayOfYear = month*30 + day
		column[i] = dayOfYear
	return column	


def numberTransformer(column):
	for i in range(len(column)):
		column[i] = float(column[i])	
	return column		