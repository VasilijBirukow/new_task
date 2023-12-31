class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
class Menter():
    def __init__(self, name, surname):
        self.name = name
        self.surname = name
        self.courses_attached = []

class Lecturer(Menter):
    def __init(self):
        pass

class Reviewer(Menter):
    def __init(self):
        pass