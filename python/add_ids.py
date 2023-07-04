import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_id_field(data):
    for i, entry in enumerate(data, start=1):
        entry["id"] = i + 1000
    return data

def main():
    file_name = 'complex_data.json'
    data = read_json_file('json/' + file_name)
    updated_data = add_id_field(data)
    write_json_file('json/' + file_name, updated_data)

if __name__ == "__main__":
    main()
