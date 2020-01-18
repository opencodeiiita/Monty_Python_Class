import csv
import json

csvfile = open('movies.csv', encoding = "utf8",errors = 'ignore')
fields = ['movieId','title','genres']
reader = csv.DictReader(csvfile, fieldnames = fields)
datalist = []
movie_genre= 'Comedy'
for row in reader:
    newrow = {'movieId' : row['movieId'], 'title':row['title'], 'genres': row['genres']}
    if(newrow['genres'].find(movie_genre)!=-1):
        datalist.append(newrow)
with open('movies.json','w') as jsonfile:
    jsonfile.write(json.dumps(datalist,indent = 4))