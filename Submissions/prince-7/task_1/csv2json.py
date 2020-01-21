import csv
import json

csvfile = open('../../../Task_1/movies.csv','r')
jsonfile = open('movies.json', 'w')
fieldnames = ['movieId','title','genres']
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    newrow = {'movieId' : row['movieId'], 'title':row['title'], 'genres': row['genres']}
    if(newrow['genres'].find('Comedy')!=-1):
        json.dump(newrow,jsonfile)
        jsonfile.write('\n')



