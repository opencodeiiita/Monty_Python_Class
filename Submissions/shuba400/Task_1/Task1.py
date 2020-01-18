import csv,json

file = open('../../../Task_1/movies.csv', encoding = "utf8",errors = 'ignore')

data = []
genre = 'Comedy'
csv_reader = csv.reader(file)
for line in csv_reader:
	josnrow = {'MovieId' : line[0], 'Title':line[1], 'Genres': line[2]}
	if(line[2].find(genre)!= -1 ):
		data.append(josnrow)

with open('movies.json','w') as newfile:
    newfile.write(json.dumps(data,indent = 4))


