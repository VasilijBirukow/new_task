class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grades(self):
        sum_grade = 0
        num= 0
        for grades in self.grades.values():
            sum_grade += grades
            num += 1
        return sum_grade / num

    def rate_hw(self, lecturer, course,  grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def __gt__(self, student):
        if isinstance(student, Student):
            return self.average_grades > student.average_grades

class Menter():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Menter):
    def grades(self):
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades}"

    def average_grades(self):
        sum_grade = 0
        num = 0
        for grades in self.grades.values():
            sum_grade += grades
            num += 1
        return sum_grade / num

    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grades > lecturer.average_grades



class Reviewer(Menter):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
