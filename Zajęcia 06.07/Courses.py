"""
Example inspired by
https://www.cs.uct.ac.za/mit_notes/python/Object_Oriented_Programming.html#exercise-1

However original code had some errors
"""
import csv

class Student:
    """
    Class represents student
    """
    student_number = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Student.student_number += 1
        self.student_id = Student.student_number
        self.classes = []

    def enroll(self, course_running):
        """
        Add student to the course
        :param course_running:
        :return:
        """
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    """
    Represents single department
    """
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, course):
        """
        Add course to department
        :param course:
        :return:
        """
        self.courses[course.course_code] = course
        return self.courses[course.course_code]


class Course:
    """
    Represents general Course which may have many editions
    """
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        self.department.add_course(self)

        self.runnings = []

    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]


class CourseRunning:
    """
    Actual course. Provides information about particular course edition
    """
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)



if __name__ == '__main__':

    python_dp = Department("Software Development Academy - Python", "Python-SDA")
    python_summer = python_dp.add_course(
        Course("Python Summer Course", "PSC", 1, python_dp)
    )
    python_actual_course = python_summer.add_running(2019)
    while True:
        first, last = input('Please provide student full name: ').split()
        bob = Student(first, last)
        bob.enroll(python_actual_course)
        if input('Continue? [y/n]: ') == 'n':
            break
    f = open(input('Provide file name: '), 'w')
    csv_writer = csv.writer(
        f, delimiter=' ', quotechar='|',
        quoting=csv.QUOTE_MINIMAL
    )
    
    for student in python_actual_course.students:
        course = python_actual_course.course
        print(course.description)
        student_row = (
            student.first_name, student.last_name,
            course.description, course.department.name,
            python_actual_course.year,
        )
        csv_writer.writerow(student_row)
    f.close()