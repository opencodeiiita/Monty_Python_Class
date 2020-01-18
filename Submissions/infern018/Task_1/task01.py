import csv,json

csvFilePath='movies.csv'
jsonFilePath='movies.json'

fields=['movieId','title','genres']

data=[]
movie_genre='Comedy'
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile,fieldnames=fields)
	for row in csvReader:
    	newrow = {'movieId' : row['movieId'], 'title':row['title'], 'genres': row['genres']}
    	if(newrow['genres'].find(movie_genre)!=-1):
        	datalist.append(newrow)
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))        