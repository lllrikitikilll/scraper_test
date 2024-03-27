import json
from pprint import pprint

with open('quotes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

new = {}

for i in data:
    new[i['name']] = new.get(i['name'], 0) + 1

print(len(data))
pprint(sorted(list(new.items()), key=lambda x: x[1]))