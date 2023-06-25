CREATE TABLE faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    dean_id INT
);

CREATE TABLE department (
    id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_id INT,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    head_instructor_id INT,
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
);

CREATE TABLE major (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department_id INT,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    hours INT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE course (
    id INT AUTO_INCREMENT PRIMARY KEY,
    major_id INT,
    name_arabic VARCHAR(255),
    name_english VARCHAR(255),
    symbol VARCHAR(255),
    description TEXT,
    credits INT,
    FOREIGN KEY (major_id) REFERENCES major(id)
);

CREATE TABLE instructor (
    id INT AUTO_INCREMENT PRIMARY KEY,
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
    id INT AUTO_INCREMENT PRIMARY KEY,
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



--------------------------------------------------------------



faculty:
    give me the description of the X faculty
    what is the symbol of the faculty X

    faculty & instructor:
        who is the dean of the faculty X (their name) - what is the name of the dean of the faculty X
        email of the dean of the faculty X
        phone number of the dean of the faculty X
        office hours of the dean of the faculty X
        ritaj id of the dean of the faculty X

        faculty & instructor & department
            department of the dean of the faculty X -- (not too important)

    list of departments in the faculty X
    list of majors in the faculty X
    list of instructors in the faculty X




department:
    give me the description of the X department
    what is the symbol of the department X

    department & instructor:
        who is the head of the department X (their name) - what is the name of the head of the department X
        email of the head of the department X
        phone number of the head of the department X
        office hours of the head of the department X
        ritaj id of the head of the department X

        department & instructor & faculty
            faculty of the department X -- (not too important)

    list of majors in the department X 
    list of instructors in the department X





major:
    give me the description of the X major
    what is the symbol of the major X
    number of total hours of the major X

    major & department:
        department of the major X -- (not too important)

    list of courses in the major X (name, symbol, description, credits) sorted by symbol
    list of course in the major X where the course is taught by the instructor Y
    list of course in the major X where the course is taught by the teaching assistant Y
    list of the courses in the major X that have the course Y as a prerequisite
    list of the courses in the major X that have the course Y as a prerequisite and are taught by the instructor Z
    list of the courses in the major X that have the course Y as a prerequisite and are taught by the teaching assistant Z
    list of the courses in the major X that have the course Y as a prerequisite and are taught by the instructor Z and the teaching assistant W -- (not too important)
    list of the courses in the major X where their credits are greater than or equal to Y
    list of the courses in the major X where their credits are less than or equal to Y
    list of the courses in the major X where their credits are greater than or equal to Y and less than or equal to Z
    list of the courses in the major X where their credits are greater than or equal to Y and less than or equal to Z and are taught by the instructor W
    list of the courses in the major X where their credits are equal to Y
    my name is omar hahahaasdsadsadsa
    list of instructors in the major X
    list of teaching assistants in the major X
    



course:
    give me the description of the X course
    what is the symbol of the course X
    number of credits of the course X
    prerequisites of the course X

    course & major:
        major of the course X -- (not too important)

    course & major & department:
        department of the course X -- (not too important)

    course & instructor:
        list of instructors of the course X 
    
    course & teaching assistant:
        list of teaching assistants of the course X

    list of the courses that have the course X as a prerequisite






instructor:
    what is the phone number of the instructor X
    what is the email of the instructor X
    what is the ritaj id of the instructor X
    what is the office hours of the instructor X

    instructor & department:
        department of the instructor X -- (not too important)

    instructor & faculty:
        faculty of the instructor X -- (not too important)

    instructor & course:
        list of courses of the instructor X
    
    instructor & teaching assistant:
        list of teaching assistants of the instructor X

    instructor & faculty:
        what is the faculty where the instructor X is the dean of
    
    instructor & department:
        what is the department where the instructor X is the head of





teaching assistant:
    what is the phone number of the teaching assistant X
    what is the email of the teaching assistant X
    what is the ritaj id of the teaching assistant X

    teaching assistant & department:
        department of the teaching assistant X -- (not too important)

    teaching assistant & course:
        list of courses of the teaching assistant X

    teaching assistant & instructor:
        list of instructors of the teaching assistant X

    
