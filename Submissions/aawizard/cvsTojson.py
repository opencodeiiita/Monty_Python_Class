import csv, json
csvFilePath='..\..\Monty_Python_Class\Task_1\movies.csv'
jasonFilePath="movieList.json"
data={}
with open(csvFilePath,encoding = "utf8",errors = 'ignore') as csvFile:
    csvReader=csv.DictReader(csvFile)
    for csvRow in csvReader:
        movieId=csvRow["movieId"]
        data[movieId]=csvRow
        
		      
with open('movies.json','w') as newfile:
    newfile.write(json.dumps(data,indent = 4))        

         
