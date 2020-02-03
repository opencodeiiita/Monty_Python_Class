import csv
import json
csvpath="movies.csv"
jsonpath="movie.json"
moviedata={}
with open(csvpath) as csvfile:
    csvread=csv.DictReader(csvfile)
    for i in csvread:
        movieId=i["movieId"]
        if("Comedy" in i["genres"]):
            moviedata[movieId]=i
with open(jsonpath,"w") as jsonfile:
    jsonfile.write(json.dumps(moviedata,indent=4))
    

