import csv, json
import pandas as pd
import os
#os.chdir("..//..")
csv_path = "../../../Task_1/movies.csv"
#print(csv_path)
json_path = "comedy_movies.json"

data = {}
with open(csv_path,  encoding='utf-8') as csvfile:
    csvReader = csv.DictReader(csvfile)
    for csvrow in csvReader:
        
        obj = {
            "movieId"; csvrow["movieId"],
            "title": csvrow["title"],
            "genres": csvrow["genres"]
            
        }
        data[csvrow["movieId"]] = obj

with open(json_path, 'w+') as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))
