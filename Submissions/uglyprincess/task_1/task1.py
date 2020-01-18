import csv, json 
csvFilePath = 'C:/Users/Aaryan/Desktop/Monty_Python_Class/Task_1/movies.csv'
jsonFilePath = 'movies.json'

data = {}

with open(csvFilePath, encoding = 'utf-8') as csvFile:
	csvReader = csv.DictReader(csvFile)
	print(csvReader)
	for csvflow in csvReader:
		movieId = csvflow["movieId"]
		data[movieId] = csvflow
		
print(data)


with open(jsonFilePath, 'w') as jsonFile:
	jsonFile.write(json.dumps(data, indent=4))
	