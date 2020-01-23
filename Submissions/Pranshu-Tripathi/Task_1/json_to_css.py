import csv, json

csvFilesPath = "../../../Task_1/movies.csv"
jsonFilePath = "Comedy.json"

datacsv = {}

with open(csvFilesPath,encoding = 'utf-8') as csvFile:
     csvReader = csv.DictReader(csvFile)
     for row in csvReader:
         movieId = row['movieId']
         datacsv[movieId] = row

# Now as the file is read we will filter the files in the list as the comedy and read it in json format

datajson = {}
for i,j in datacsv.items():
    if j['genres'] == 'Comedy':
        datajson[i]=j


with open(jsonFilePath,'w') as jsonFile:
    jsonFile.write(json.dumps(datajson,indent = 5))
