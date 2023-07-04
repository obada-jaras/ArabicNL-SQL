CREATE TABLE faculty (
    id INT PRIMARY KEY,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    dean_id INT
);

CREATE TABLE department (
    id INT PRIMARY KEY,
    faculty_id INT,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    head_instructor_id INT,
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
);

CREATE TABLE major (
    id INT PRIMARY KEY,
    department_id INT,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    hours INT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE course (
    id INT PRIMARY KEY,
    major_id INT,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    credits INT,
    FOREIGN KEY (major_id) REFERENCES major(id)
);

CREATE TABLE instructor (
    id INT PRIMARY KEY,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(255),
    ritaj_id VARCHAR(255),
    office_hours VARCHAR(255),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE teaching_assistant (
    id INT PRIMARY KEY,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(255),
    ritaj_id VARCHAR(255),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE course_prerequisite (
    course_id INT,
    prerequisite_id INT,
    PRIMARY KEY (course_id, prerequisite_id),
    FOREIGN KEY (course_id) REFERENCES course(id),
    FOREIGN KEY (prerequisite_id) REFERENCES course(id)
);

CREATE TABLE instructor_course (
    instructor_id INT,
    course_id INT,
    PRIMARY KEY (instructor_id, course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructor(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);

CREATE TABLE ta_course (
    ta_id INT,
    course_id INT,
    PRIMARY KEY (ta_id, course_id),
    FOREIGN KEY (ta_id) REFERENCES teaching_assistant(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);

ALTER TABLE faculty
ADD FOREIGN KEY (dean_id) REFERENCES instructor(id);