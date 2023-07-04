import json

with open('json/data_examples.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

new_data = []

for item in data:
    if 'examples' in item:
        for example in item['examples']:
            new_data.append({
                'Arabic-Query': example['Arabic-Query'],
                'SQL-Query': example['SQL-Query']
            })
    else:
        new_data.append({
            'Arabic-Query': item['Arabic-Query'],
            'SQL-Query': item['SQL-Query']
        })

with open('json/flattened_data.json', 'w', encoding='utf-8') as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)
