import json

class FileManager:
    @staticmethod
    def load_json_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    @staticmethod
    def load_txt_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read().splitlines()

    @staticmethod
    def save_to_json_file(filepath, data):
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)




class SQLMapper:
    @staticmethod
    def map_real_id_to_sql_query(data_examples):
        return {example['id']: SQLMapper.extract_sql_query_from_example(example) for example in data_examples}
    
    @staticmethod
    def extract_sql_query_from_example(example):
        for ex in example['examples']:
            if 'SQL-Query' in ex:
                return ex['SQL-Query'].strip()
        return None

    @staticmethod
    def map_query_id_to_real_id(queries):
        return {query_id: query['real_id'] for query_id, query in queries.items()}





class VariantProcessor:
    @staticmethod
    def generate_output(variants, exclude_answers, exclude_submissions, query_id_to_real_id, id_to_sql):
        return [VariantProcessor.create_output_item(variant['answer'].strip(), VariantProcessor.get_sql_query_for_variant(variant, query_id_to_real_id, id_to_sql)) 
                for variant_id, variant in variants.items() 
                if VariantProcessor.should_include_variant(variant_id, variant['answer'].strip(), variant['submissionId'], exclude_answers, exclude_submissions)]

    @staticmethod
    def remove_duplicates(output):
        output_set = set(json.dumps(item) for item in output)
        return [json.loads(item) for item in output_set]

    @staticmethod
    def should_include_variant(variant_id, trimmed_answer, submission_id, exclude_answers, exclude_submissions):
        return variant_id not in exclude_answers and submission_id not in exclude_submissions and trimmed_answer

    @staticmethod
    def get_sql_query_for_variant(variant, query_id_to_real_id, id_to_sql):
        real_id = query_id_to_real_id.get(variant['query_id'])
        return id_to_sql.get(real_id)

    @staticmethod
    def create_output_item(input_text, output_text):
        return {
            "input": input_text,
            "output": output_text
        }





def main():
    file_manager = FileManager()
    sql_mapper = SQLMapper()
    variant_processor = VariantProcessor()

    queries = file_manager.load_json_file('json/exported_database/queries.json')
    variants = file_manager.load_json_file('json/exported_database/variants.json')
    data_examples = file_manager.load_json_file('json/data_examples.json')
    exclude_submissions = file_manager.load_txt_file('text/exclude/submissions.txt')
    exclude_answers = file_manager.load_txt_file('text/exclude/answers.txt')

    id_to_sql = sql_mapper.map_real_id_to_sql_query(data_examples)
    query_id_to_real_id = sql_mapper.map_query_id_to_real_id(queries)

    output = variant_processor.generate_output(variants, exclude_answers, exclude_submissions, query_id_to_real_id, id_to_sql)

    output = variant_processor.remove_duplicates(output)

    file_manager.save_to_json_file('json/data_examples_variants.json', output)

    print(f"The new output file contains {len(output)} items.")

if __name__ == "__main__":
    main()
