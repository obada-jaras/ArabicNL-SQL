import json

def load_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_json_file(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_real_id_to_sql_query_map(data_examples):
    return {example['id']: get_sql_query_from_example(example) for example in data_examples}
    
def get_sql_query_from_example(example):
    for ex in example['examples']:
        if 'SQL-Query' in ex:
            return ex['SQL-Query'].strip()
    return None

def get_query_id_to_real_id_map(queries):
    return {query_id: query['real_id'] for query_id, query in queries.items()}

def add_variations_to_data_examples(data_examples, queries, variants):
    query_id_to_real_id = get_query_id_to_real_id_map(queries)

    for example in data_examples:
        for ex in example['examples']:
            ex['variations'] = get_variations_for_example(example['id'], query_id_to_real_id, variants)
            
    return data_examples

def get_variations_for_example(real_id, query_id_to_real_id, variants):
    variations = []

    for variant in variants.values():
        if is_variant_for_example(real_id, variant, query_id_to_real_id):
            variations.append(variant['answer'])
    
    return variations

def is_variant_for_example(real_id, variant, query_id_to_real_id):
    return variant['query_id'] in query_id_to_real_id and query_id_to_real_id[variant['query_id']] == real_id

def main():
    data_examples = load_json_file('json/data_examples.json')
    queries = load_json_file('json/exported_database/queries.json')
    variants = load_json_file('json/exported_database/variants.json')

    updated_data_examples = add_variations_to_data_examples(data_examples, queries, variants)

    save_to_json_file('json/simple_data_with_examples_and_variations.json', updated_data_examples)

    print(f"The new output file contains {len(updated_data_examples)} items.")

if __name__ == "__main__":
    main()
