import csv, json,os

current = os.getcwd()
os.chdir("../../../Task_1")
csv_file = open("movies.csv", encoding="utf-8")
os.chdir(current)
json_file = open("csv_to_json_converted.json","w")

csv_reader = csv.reader(csv_file);

csv_list = list(csv_reader)

headings = csv_list[0]
json_file.write("[\n\t")
for i in range(1,len(csv_list)):
    json_file.write("{\n\t")
    for j in range(len(headings)):
        json_file.write(json.dumps(headings[j]))
        json_file.write(":")
        json_file.write(json.dumps(csv_list[i][j])) 
        if (j==len(headings)-1):
            pass
        else:
            json_file.write(",\n\t")
    if i!=len(csv_list)-1:
        json_file.write("\n\t},\n\t")
    else:
        json_file.write("\n\t}\n")
json_file.write("]")
