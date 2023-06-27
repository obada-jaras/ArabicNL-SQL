import json

def count_entries(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        num_entries = len(data)
        return num_entries

file_path = 'data.json'
num_entries = count_entries(file_path)
print(f"The number of entries in {file_path} is: {num_entries}")
