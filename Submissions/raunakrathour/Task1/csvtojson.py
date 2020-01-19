import csv,json
csvpath= "movies.csv"
jsonpath="comedy.json"
temp = []

with open(csvpath) as csvfile:
	csvreader=csv.DictReader(csvfile)
	for row in csvreader:
		hid = {'movieId' : row['movieId'],'title':row['title'],'genres': row['genres']}
		if hid['genres'].find('Comedy')!=-1:
			temp.append(hid)
with open(jsonpath,"w") as jsonfile:
	jsonfile.write(json.dumps(temp,indent=4))
