import json
import random

TAGS = [
    "faculty-name",
    "faculty-symbol",
    "department-name",
    "department-symbol",
    "major-name",
    "major-symbol",
    "course-name",
    "course-symbol",
    "instructor-name",
    "assistant-name",
    "credits",
    "min-credits",
    "max-credits"
]

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_random_replacement_value(dummy_data, tag):
    if tag == "course-name":
        return random.choice(dummy_data["course"])["course-name"]["name-ar"]
    elif tag == "course-symbol":
        return random.choice(dummy_data["course"])["course-symbol"]
    elif tag in ["instructor-name", "assistant-name"]:
        return random.choice(dummy_data[tag.split('-')[0]])
    elif tag == "credits":
        return str(random.randint(1, 5))
    elif tag == "min-credits":
        return str(random.randint(1, 2))
    elif tag == "max-credits":
        return str(random.randint(3, 5))
    else:
        return random.choice(dummy_data[tag.split('-')[0]])[tag]

def replace_tags_in_query(query, replacements):
    for tag, replacement_value in replacements.items():
        tag_to_find = f'[{tag}]'
        while tag_to_find in query:
            query = query.replace(tag_to_find, replacement_value, 1)
    return query

def add_examples_field(data, dummy_data):
    for entry in data:
        entry["examples"] = []
        replacements = {tag: get_random_replacement_value(dummy_data, tag) for tag in TAGS if f'[{tag}]' in entry["Arabic-Query"] or f'[{tag}]' in entry["SQL-Query"]}
        example = {}
        example["labels"] = replacements
        example["Arabic-Query"] = replace_tags_in_query(entry["Arabic-Query"], replacements)
        example["SQL-Query"] = replace_tags_in_query(entry["SQL-Query"], replacements)
        entry["examples"].append(example)
    return data

def main():
    data = read_json_file('json/complex_data.json')
    dummy_data = read_json_file('json/dummy.json')
    updated_data = add_examples_field(data, dummy_data)
    write_json_file('json/complex_data_examples.json', updated_data)

if __name__ == "__main__":
    main()
