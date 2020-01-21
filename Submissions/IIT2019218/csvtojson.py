import csv
import json



given  = [ 'movieId' , 'title' , 'genres' ]



data = []

with open ('movies.csv' , errors='ignore') as csvFile:
    fileswanted = csv.DictReader(csvFile , fieldnames=given )

    for row in fileswanted:
        comedies = { 'movieId' : row['movieId'], 'title' : row['title'], 'genres' :row['genres']}
        if(comedies['genres'].find('Comedy') != -1):
            data.append(comedies)


with open('comedymovies.json' , 'w') as jsonFile :
    jsonFile.write(json.dumps(data, indent=4))
