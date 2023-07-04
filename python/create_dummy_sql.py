import json
import random


def create_insert_for_faculty(faculty_data, instructor_ids):
    statements = []
    for i, faculty in enumerate(faculty_data, start=1):
        dean_id = instructor_ids.pop() if instructor_ids else 'NULL'
        statements.append(
            f"INSERT INTO faculty(id, name_arabic, name_english, symbol, description, dean_id) "
            f"VALUES ({i}, '{faculty['faculty-name']}', 'name english - faculty - {faculty['faculty-symbol']}', '{faculty['faculty-symbol']}', 'Description for faculty {i}', {dean_id});")
    return statements

def update_faculty_with_dean(faculty_count, instructor_ids):
    statements = []
    for i in range(1, faculty_count + 1):
        dean_id = instructor_ids.pop()
        statements.append(
            f"UPDATE faculty SET dean_id = {dean_id} WHERE id = {i};")
    return statements


def create_insert_for_department(department_data, faculty_count, instructor_ids):
    statements = []
    for i, department in enumerate(department_data, start=1):
        head_instructor_id = 'NULL' if instructor_ids is None else instructor_ids.pop()
        statements.append(
            f"INSERT INTO department(id, faculty_id, name_arabic, name_english, symbol, description, head_instructor_id) "
            f"VALUES ({i}, {random.randint(1, faculty_count)}, '{department['department-name']}', 'name english - department - {department['department-symbol']}', '{department['department-symbol']}', 'Description for department {i}', {head_instructor_id});")
    return statements

def update_department_with_head(department_count, instructor_ids):
    statements = []
    for i in range(1, department_count + 1):
        head_id = instructor_ids.pop()
        statements.append(
            f"UPDATE department SET head_instructor_id = {head_id} WHERE id = {i};")
    return statements

def create_insert_for_major(major_data, department_count):
    statements = []
    for i, major in enumerate(major_data, start=1):
        statements.append(
            f"INSERT INTO major(id, department_id, name_arabic, name_english, symbol, description, hours) "
            f"VALUES ({i}, {random.randint(1, department_count)}, '{major['major-name']}', 'name english - major - {major['major-symbol']}', '{major['major-symbol']}', 'Description for major {i}', {random.randint(120, 165)});")
    return statements


def create_insert_for_course(course_data, major_count):
    statements = []
    for i, course in enumerate(course_data, start=1):
        statements.append(
            f"INSERT INTO course(id, major_id, name_arabic, name_english, symbol, description, credits) "
            f"VALUES ({i}, {random.randint(1, major_count)}, '{course['course-name']['name-ar']}', '{course['course-name']['name_en']}', '{course['course-symbol']}', 'Description for course {i}', {int(course['credits'])});")
    return statements


def create_insert_for_instructor(instructor_data, department_count):
    statements = []
    for i, instructor in enumerate(instructor_data, start=1):
        statements.append(
            f"INSERT INTO instructor(id, name_arabic, name_english, phone_number, email, ritaj_id, office_hours, department_id) "
            f"VALUES ({i}, '{instructor}', 'Instructor {i}', '{i}{i}{i}-{i}', 'instructor_email_{i}@example.com', 'RITAJ_I_{i}', 'Office Hours {i}', {random.randint(1, department_count)});")
    return statements


def create_insert_for_ta(ta_data, department_count):
    statements = []
    for i, ta in enumerate(ta_data, start=1):
        statements.append(
            f"INSERT INTO teaching_assistant(id, name_arabic, name_english, phone_number, email, ritaj_id, department_id) "
            f"VALUES ({i}, '{ta}', 'TA {i}', '{i}{i}{i}-{i}', 'assistant_email_{i}@example.com', 'RITAJ_A_{i}', {random.randint(1, department_count)});")
    return statements


def create_insert_for_course_prerequisite(course_count):
    statements = []
    for i in range(1, course_count + 1):
        prerequisite_count = random.randint(0, 2)
        prerequisites = random.sample(
            range(1, course_count + 1), prerequisite_count)
        for prerequisite in prerequisites:
            if prerequisite != i:  # A course cannot be a prerequisite of itself
                statements.append(
                    f"INSERT INTO course_prerequisite(course_id, prerequisite_id) VALUES ({i}, {prerequisite});"
                )
    return statements


def create_insert_for_instructor_course(instructor_count, course_count):
    statements = []
    for i in range(1, instructor_count + 1):
        course_count_for_instructor = random.randint(1, 3)
        courses = random.sample(
            range(1, course_count + 1), course_count_for_instructor)
        for course in courses:
            statements.append(
                f"INSERT INTO instructor_course(instructor_id, course_id) VALUES ({i}, {course});"
            )
    return statements


def create_insert_for_ta_course(ta_count, course_count):
    statements = []
    for i in range(1, ta_count + 1):
        course_count_for_ta = random.randint(1, 3)
        courses = random.sample(
            range(1, course_count + 1), course_count_for_ta)
        for course in courses:
            statements.append(
                f"INSERT INTO ta_course(ta_id, course_id) VALUES ({i}, {course});"
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
    course_count = len(data['course'])
    ta_count = len(data['assistant'])

    # Create a set of instructor IDs to ensure each instructor can be a dean or head at most once.
    instructor_ids = set(range(1, instructor_count + 1))

    all_statements = []

    # First, create faculties without assigning deans.
    all_statements.extend(create_insert_for_faculty(data['faculty'], None))

    # Create departments without assigning heads.
    all_statements.extend(create_insert_for_department(data['department'], faculty_count, None))

    # Then, create instructors and assign them as deans and heads.
    all_statements.extend(create_insert_for_instructor(data['instructor'], department_count))
    all_statements.extend(update_faculty_with_dean(faculty_count, instructor_ids))
    all_statements.extend(update_department_with_head(department_count, instructor_ids))

    # Now we can create the remaining entities.
    all_statements.extend(create_insert_for_major(data['major'], department_count))
    all_statements.extend(create_insert_for_course(data['course'], major_count))
    all_statements.extend(create_insert_for_ta(data['assistant'], department_count))

    # Now we can create the inserts for the other tables.
    all_statements.extend(create_insert_for_course_prerequisite(course_count))
    all_statements.extend(create_insert_for_instructor_course(instructor_count, course_count))
    all_statements.extend(create_insert_for_ta_course(ta_count, course_count))

    write_to_file(all_statements, sql_filename)


generate_sql_inserts('json/dummy.json', 'sql/insert-dummy_data.sql')
