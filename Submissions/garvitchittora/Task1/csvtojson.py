import csv
import json
import os

path1 = '..\..\..\Task_1\movies.csv'

dict = []

with open(path1,'r', encoding="utf8") as csv_file:
	fieldnames = ("movieId","title","genres")
	csv_reader = csv.DictReader(csv_file,fieldnames)

	for line in csv_reader:
		b = line['genres'].split('|')
		for c in b:
			if c == 'Comedy':
				dict.append(line)
				break
					
with open('csv2json.json','w',encoding = "utf8") as json_file:
	json.dump(dict,json_file,indent = 4)





