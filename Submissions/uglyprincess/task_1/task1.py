import csv, json 
import pandas as pn
import numpy as nd
jsonFilePath = 'new.json'

data = {}

data = pn.read_csv("C:/Users/Aaryan/Desktop/Monty_Python_Class/Task_1/movies.csv")
data.columns = [column.replace(" ", "_") for column in data.columns]
data.query('genres=="Comedy"')

print(data)

data.columns = [column.replace("_", " ") for column in data.columns]

data = data.to_json()

with open(jsonFilePath, 'w') as jsonFile:
	jsonFile.write(json.dumps(data, indent=4))
	