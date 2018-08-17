import json
import csv


def parseFilters(cell):
    filters = []
    fields = cell.split('|')
    print(fields)
    for field in fields:
        keyPair = field.split(':')
        print(keyPair)
        filters.append({keyPair[0]:keyPair[1]})
    return filters

questions_array = []

with open("newFile.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        temp_dict = {}
        temp_dict['question'] = row[0]
        temp_dict['answer'] = row[1]
        if not row[2]:
            temp_dict['filters'] = []
        else:
            temp_dict['filters'] = parseFilters(row[2])
        questions_array.append(temp_dict)
with open('data.json', 'w') as outfile:
    json.dump(questions_array, outfile)
