USE Tech4Girls_DB

--creating a course table
CREATE TABLE courses(
    id INT AUTO_INCREAMENT PRIMARY KEY,
    course_name VARCHAR(100)
);

--creating a user_courses table to many-to- many-relationship
CREATE TABLE user-courses(
    user_id INT,
    course_id INT,
    PRIMARY KEY (user_id, course_id),
    FOEIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE
    );

    INSERT INTO courses (course_name)
    VALUES('statistics'),
          ('geography'),
          ('computer science');

--inserting data into user_courses to demonstrate many-to-many relationship
INSERT INTO user_courses (user_id, course_id)
VALUES (1, 1), --ama enrolled in satatistics
(1, 2), --ama enrolled in geography
(2, 2), --abena enrolled in geography
(2, 3), --abena enrolled in computer science
(3, 1), --adjoa enrolled in statistics
(3, 3); --adjoa enrolled in computer science