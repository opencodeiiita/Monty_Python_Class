import json
import csv
inpath='movies.csv'
opath='convfilemovies.json'
given=['movieId','title','genres']
tofind='Comedy'
data=[]
with open(inpath,errors='ignore') as csvFile:
    myre=csv.DictReader(csvFile, fieldnames=given)
    for row in myre:
        guts={'movieId' : row['movieId'], 'title':row['title'], 'genres': row['genres']}
        if(guts['genres'].find(tofind)!=-1):
            data.append(guts)
with open(opath,'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=5))
