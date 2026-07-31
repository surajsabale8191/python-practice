class Student:
    school="ABC School"

    def __init__(self, name):
        self.name=name

    def show_name(self):
        print("Student Name :", self.name)

    @classmethod
    def show_school(cls):
        print("School name :",cls.school)

    @staticmethod
    def greet():
        print("Welcome students")


stud1=Student("Sanjay")
stud1.show_name()
Student.show_school()
Student.greet()
