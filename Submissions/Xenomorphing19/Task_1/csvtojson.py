import csv
import json

csvfile = open('filter.csv', 'r')
jsonfile = open('filter.json', 'w')

reader = csv.DictReader( csvfile)
for row in csvfile:
    out =str(row)+'\n'
    jsonfile.write(out)
