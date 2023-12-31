from task_three import *
students = []
def new_student(student):
    if isinstance(student, Student):
        students.append(student)
    else:
        print("Ошибка")

def average_grades_students(students, cours):
    sum_grades = []
    num = 0
    for student in students:
        if cours in student.courses_in_progress:
            sum_grades.append(student.grades[cours])
            num += 1
    return sum(sum_grades) / num

lecturers = []
def new_lecturer(lecturer):
    if isinstance(lecturer, Lecturer):
        lecturers.append(lecturer)
    else:
        print("Ошибка")

def average_grades_lecturers(lecrurers, cours):
    sum_grades = []
    num = 0
    for lecrurer in lecrurers:
        if cours in lecrurer.courses_in_progress:
            sum_grades.append(lecrurer.grades[cours])
            num += 1
    return sum(sum_grades) / num


