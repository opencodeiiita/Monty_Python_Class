import csv
import json

with open('C:\\Users\\SAKSHAM\\Desktop\\OpenCode20\\2-Python t1\\Monty_Python_Class\\Task_1\\movies.csv','r', encoding="utf8") as csv_file:
	fieldnames = ("movieId","title","genres")
	csv_reader = csv.DictReader(csv_file,fieldnames)

	
		
		

	with open('csv2json.json','w', encoding="utf8") as json_file:

		for line in csv_reader:
			b = line['genres'].split('|')

			for c in b:
				if c == 'Comedy':
					json.dump(line,json_file,indent = 4)
					json_file.write('\n')
