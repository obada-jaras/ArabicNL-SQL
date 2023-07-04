import json
import random

def create_insert_for_faculty(faculty_data, dean_count):
    statements = []
    for i, faculty in enumerate(faculty_data, start=1):
        statements.append(
            f"INSERT INTO faculty(id, name_arabic, name_english, symbol, description, dean_id) "
            f"VALUES ({i}, '{faculty['faculty-name']}', 'name english - faculty - {faculty['faculty-symbol']}', '{faculty['faculty-symbol']}', 'Description {i}', {random.randint(1, dean_count)});"
        )
    return statements

def create_insert_for_department(department_data, faculty_count):
    statements = []
    for i, department in enumerate(department_data, start=1):
        statements.append(
            f"INSERT INTO department(id, faculty_id, name_arabic, name_english, symbol, description, head_instructor_id) "
            f"VALUES ({i}, {random.randint(1, faculty_count)}, '{department['department-name']}', 'name english - department - {department['department-symbol']}', '{department['department-symbol']}', 'Description {i}', {random.randint(1, 100)});"
        )
    return statements

def create_insert_for_major(major_data, department_count):
    statements = []
    for i, major in enumerate(major_data, start=1):
        statements.append(
            f"INSERT INTO major(id, department_id, name_arabic, name_english, symbol, description, hours) "
            f"VALUES ({i}, {random.randint(1, department_count)}, '{major['major-name']}', 'name english - major - {major['major-symbol']}', '{major['major-symbol']}', 'Description for major {i}', {random.randint(120, 165)});"
        )
    return statements

def create_insert_for_course(course_data, major_count):
    statements = []
    for i, course in enumerate(course_data, start=1):
        statements.append(
            f"INSERT INTO course(id, major_id, name_arabic, name_english, symbol, description, credits) "
            f"VALUES ({i}, {random.randint(1, major_count)}, '{course['course-name']['name-ar']}', '{course['course-name']['name_en']}', '{course['course-symbol']}', 'Description for course {i}', {int(course['credits'])});"
        )
    return statements

def create_insert_for_instructor(instructor_data, department_count):
    statements = []
    for i, instructor in enumerate(instructor_data, start=1):
        statements.append(
            f"INSERT INTO instructor(id, name_arabic, name_english, phone_number, email, ritaj_id, office_hours, department_id) "
            f"VALUES ({i}, '{instructor}', 'Instructor {i}', '{i}{i}{i}-{i}', 'instructor_email_{i}@example.com', 'RITAJ_I_{i}', 'Office Hours {i}', {random.randint(1, department_count)});"
        )
    return statements

def create_insert_for_ta(ta_data, department_count):
    statements = []
    for i, ta in enumerate(ta_data, start=1):
        statements.append(
            f"INSERT INTO teaching_assistant(id, name_arabic, name_english, phone_number, email, ritaj_id, department_id) "
            f"VALUES ({i}, '{ta}', 'TA {i}', '{i}{i}{i}-{i}', 'assistant_email_{i}@example.com', 'RITAJ_A_{i}', {random.randint(1, department_count)});"
        )
    return statements

def write_to_file(statements, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for statement in statements:
            f.write(statement + "\n")

def generate_sql_inserts(json_filename, sql_filename):
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    instructor_count = len(data['instructor'])
    faculty_count = len(data['faculty'])
    department_count = len(data['department'])
    major_count = len(data['major'])

    all_statements = []
    all_statements.extend(create_insert_for_faculty(data['faculty'], instructor_count))
    all_statements.extend(create_insert_for_department(data['department'], faculty_count))
    all_statements.extend(create_insert_for_major(data['major'], department_count))
    all_statements.extend(create_insert_for_course(data['course'], major_count))
    all_statements.extend(create_insert_for_instructor(data['instructor'], department_count))
    all_statements.extend(create_insert_for_ta(data['assistant'], department_count))

    write_to_file(all_statements, sql_filename)


generate_sql_inserts('json/dummy.json', 'sql/output.sql')
