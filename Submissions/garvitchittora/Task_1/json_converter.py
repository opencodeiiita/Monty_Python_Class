line_count=0
json_output = {}
import csv
import json
#done
with open("file.csv", mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        json_output[row[0]] = row[1]
        line_count += 1
    print(f'Processed {line_count} lines.')
    print(json_output)
    with open('data.json', 'w') as outfile:
        json.dump(json_output, outfile)
