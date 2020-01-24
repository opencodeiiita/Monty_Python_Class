
import csv, json
csvFilePath='movies.csv'
jasonFilePath="movieList.json"
data={}
comedy={}
with open(csvFilePath,encoding = "utf8",errors = 'ignore') as csvFile:
    csvReader=csv.DictReader(csvFile)
    for csvRow in csvReader:
        movieId=csvRow["movieId"]
        data[movieId]=csvRow
        if csvRow["genres"]=="Comedy":
            
            comedy[movieId]=csvRow
		      
with open('movies.json','w') as newfile:
    newfile.write(json.dumps(comedy,indent = 4))        

         
