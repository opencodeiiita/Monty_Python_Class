import csv,json

csvFilePath='movies.csv'
jsonFilePath='movies.json'

data={}
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for csvRow in csvReader:
		id = csvRow["id"]
		data[id] = csvRow
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))        