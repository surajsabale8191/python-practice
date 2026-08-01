class Student:
    def __init__(self,marks):
        self.__marks=marks

    #Getter
    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        if 0<=value<=100:
            self.__marks=value
            
        else:
             print("Marks must be between 0 and 100.")


    @marks.deleter    
    def marks(self):
        print("marks removed")

        del self.__marks

student=Student(65)
print("Current Marks:", student.marks)
student.marks=120
del student.marks
