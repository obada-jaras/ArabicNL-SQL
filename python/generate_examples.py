import json
import random


# [faculty-name]
def replace_faculty_name(entry, dummy_data):
    if '[faculty-name]' in entry['Arabic-Query']:
        faculty = random.choice(dummy_data['faculty'])
        entry['examples'] = [
            {"label": faculty['faculty-name'],
             "Arabic-Query": entry['Arabic-Query'].replace('[faculty-name]', faculty['faculty-name']),
             "SQL-Query": entry['SQL-Query'].replace('[faculty-name]', faculty['faculty-name'])
             }]


# [faculty-symbol]
def replace_faculty_symbol(entry, dummy_data):
    if '[faculty-symbol]' in entry['Arabic-Query']:
        faculty = random.choice(dummy_data['faculty'])
        entry['examples'] = [
            {"label": faculty['faculty-symbol'],
             "Arabic-Query": entry['Arabic-Query'].replace('[faculty-symbol]', faculty['faculty-symbol']),
             "SQL-Query": entry['SQL-Query'].replace('[faculty-symbol]', faculty['faculty-symbol'])
             }]


# [department-name]
def replace_department_name(entry, dummy_data):
    if '[department-name]' in entry['Arabic-Query']:
        department = random.choice(dummy_data['department'])
        entry['examples'] = [
            {"label": department['department-name'],
             "Arabic-Query": entry['Arabic-Query'].replace('[department-name]', department['department-name']),
             "SQL-Query": entry['SQL-Query'].replace('[department-name]', department['department-name'])
             }]


# [department-symbol]
def replace_department_symbol(entry, dummy_data):
    if '[department-symbol]' in entry['Arabic-Query']:
        department = random.choice(dummy_data['department'])
        entry['examples'] = [
            {"label": department['department-symbol'],
             "Arabic-Query": entry['Arabic-Query'].replace('[department-symbol]', department['department-symbol']),
             "SQL-Query": entry['SQL-Query'].replace('[department-symbol]', department['department-symbol'])
             }]


# [major-name]
def replace_major_name(entry, dummy_data):
    if '[major-name]' in entry['Arabic-Query']:
        major = random.choice(dummy_data['major'])
        entry['examples'] = [
            {"label": major['major-name'],
             "Arabic-Query": entry['Arabic-Query'].replace('[major-name]', major['major-name']),
             "SQL-Query": entry['SQL-Query'].replace('[major-name]', major['major-name'])
             }]


# [major-symbol]
def replace_major_symbol(entry, dummy_data):
    if '[major-symbol]' in entry['Arabic-Query']:
        major = random.choice(dummy_data['major'])
        entry['examples'] = [
            {"label": major['major-symbol'],
             "Arabic-Query": entry['Arabic-Query'].replace('[major-symbol]', major['major-symbol']),
             "SQL-Query": entry['SQL-Query'].replace('[major-symbol]', major['major-symbol'])
             }]


# [course-name]
def replace_course_name(entry, dummy_data):
    if '[course-name]' in entry['Arabic-Query']:
        course = random.choice(dummy_data['course'])
        entry['examples'] = [
            {"label": course['course-name']['name-ar'],
             "Arabic-Query": entry['Arabic-Query'].replace('[course-name]', course['course-name']['name-ar']),
             "SQL-Query": entry['SQL-Query'].replace('[course-name]', course['course-symbol'])
             }]


# [course-symbol]
def replace_course_symbol(entry, dummy_data):
    if '[course-symbol]' in entry['Arabic-Query']:
        course = random.choice(dummy_data['course'])
        entry['examples'] = [
            {"label": course['course-symbol'],
             "Arabic-Query": entry['Arabic-Query'].replace('[course-symbol]', course['course-symbol']),
             "SQL-Query": entry['SQL-Query'].replace('[course-symbol]', course['course-symbol'])
             }]


# [instructor-name]
def replace_instructor_name(entry, dummy_data):
    if '[instructor-name]' in entry['Arabic-Query']:
        instructor = random.choice(dummy_data['instructor'])
        entry['examples'] = [
            {"label": instructor,
             "Arabic-Query": entry['Arabic-Query'].replace('[instructor-name]', instructor),
             "SQL-Query": entry['SQL-Query'].replace('[instructor-name]', instructor)
             }]


# [ta-name]
def replace_ta_name(entry, dummy_data):
    if '[ta-name]' in entry['Arabic-Query']:
        ta = random.choice(dummy_data['assistant'])
        entry['examples'] = [
            {"label": ta,
             "Arabic-Query": entry['Arabic-Query'].replace('[ta-name]', ta),
             "SQL-Query": entry['SQL-Query'].replace('[ta-name]', ta)
             }]


def replace_tags(data_file, dummy_file, output_file):
    with open(data_file, 'r', encoding='utf-8') as df, open(dummy_file, 'r', encoding='utf-8') as dummyf:
        data = json.load(df)
        dummy_data = json.load(dummyf)

    for entry in data:
        replace_faculty_name(entry, dummy_data)
        replace_faculty_symbol(entry, dummy_data)
        replace_department_name(entry, dummy_data)
        replace_major_name(entry, dummy_data)
        replace_course_name(entry, dummy_data)
        replace_instructor_name(entry, dummy_data)
        replace_ta_name(entry, dummy_data)

    with open(output_file, 'w', encoding='utf-8') as outf:
        json.dump(data, outf, ensure_ascii=False, indent=4)


replace_tags('json/data.json', 'json/dummy.json', 'json/data_examples.json')
