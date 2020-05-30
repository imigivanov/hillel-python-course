"""
Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер группы, успеваемость (дикт из элементов).

Создать класс Group с атрибутом name

Создать класс генератор результатов, который будет принимать на вход данные о студентах и иметь возможность вывода
фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
"""


class Group(object):

    def __init__(self, group_name):
        self.group_name = group_name


class Student(Group):

    def __init__(self, name, surname, initials, group_name, performance):
        self.name = name
        self.surname = surname
        self.initials = initials
        super().__init__(group_name)
        self.performance = performance

class Results(object):
    pass




test_student = [('Ihor', 'Ivanov', 'IIN', 'Applied Linguistics', {'math': 5, 'english': 3}), ('Ivan', 'Ivanov', 'III', 'Python engineering', {'math': 5, 'english': 5})]

students = []
for stud in test_student:
    students.append(Student(*stud))

print(students[0].__dict__)

