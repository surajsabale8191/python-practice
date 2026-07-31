class Student:
    def __init__(self, name):
        self.name=name

    def display(self):
        print("Student Name :",self.name)

stud1=Student("Sanju")
stud2=Student("Jaggu")

stud1.display()
stud2.display()