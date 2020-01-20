import csv, json

csvFilePath = "../../../Task_1/movies.csv"
jsonFilePath = "try.json"

data = {}

with open(csvFilePath, encoding = 'utf-8') as csvFile:
	csvReader = csv.DictReader(csvFile)
	for rows in csvReader:
		movieId = rows['movieId']
		data[movieId] = rows

# [v for v in data.values() if 'Comedy' in data.values()]

datanew = {}

for k,v in data.items():
	if v['genres']=='Comedy':
		datanew[k]=v

with open(jsonFilePath, 'w') as jsonFile:
	jsonFile.write(json.dumps(datanew, indent = 4))