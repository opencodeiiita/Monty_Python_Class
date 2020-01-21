import csv

def read_from_file(csv_file):
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

data_from_first_csv = read_from_file("../../../Task_1/movies.csv")

output_data = []
i=int(1)
for row in data_from_first_csv:
    k=row[2].split('|')
    if row[2]=='Comedy':
        row[0]=i
        i=i+1
        output_data.append(row)
    elif k.count('Comedy')>0:
        row[0]=str(i)
        i=i+1
        output_data.append(row)
    

    

with open("filter.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(output_data)


