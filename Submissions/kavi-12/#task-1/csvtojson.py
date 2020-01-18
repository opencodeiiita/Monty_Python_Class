import csv, json
csv_path = "movies.csv"
json_path = "movies.json"

data = {}
with open(csv_path,  encoding='utf-8') as csvfile:
    csvReader = csv.DictReader(csvfile)
    for csvrow in csvReader:
        
        obj = {
            "title": csvrow["title"],
            "genres": csvrow["genres"]
            
        }
        data[csvrow["movieId"]] = obj

with open(json_path, 'w+') as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))