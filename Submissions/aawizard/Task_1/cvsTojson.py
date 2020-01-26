
import csv, json
csvFilePath='movies.csv'
jasonFilePath="movieList.json"
data={}
comedy=[]
fields = ['movieId','title','genres']
with open(csvFilePath,encoding = "utf8",errors = 'ignore') as csvFile:
    csvReader=csv.DictReader(csvFile,fieldnames=fields)
    for csvRow in csvReader:
        newrow = {'movieId' : csvRow['movieId'], 'title':csvRow['title'], 'genres': csvRow['genres']}
        if(newrow['genres'].find('Comedy')!=-1):
            comedy.append(newrow)
        
#writing to json		      
with open('movies.json','w') as newfile:
    newfile.write(json.dumps(comedy,indent = 4))        

         
