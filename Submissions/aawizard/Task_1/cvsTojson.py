import csv, json
csvFilePath='E:\openCode\Monty_Python_Class\Task_1\movies.csv'
jasonFilePath="movieList.json"
data={}
with open(csvFilePath,encoding = "utf8",errors = 'ignore') as csvFile:
    csvReader=csv.DictReader(csvFile)
    for csvRow in csvReader:
        movieId=csvRow["movieId"]
        data[movieId]=csvRow
        # row={"movieId": csvRow[0], "title":csvRow[1],"genres":csvRow[2]}
        # if(csvRow[2].find(genre)!= -1 ):
        #     data.append(row)
		      
with open('movies.json','w') as newfile:
    newfile.write(json.dumps(data,indent = 4))        

         
