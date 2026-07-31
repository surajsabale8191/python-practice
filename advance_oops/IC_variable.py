class Employee:
    company="OpenAI"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

emp1=Employee("Samir",25000)
emp2=Employee("Sanjay",60000)

print(emp1.company, emp1.name, emp1.salary)
print(emp2.company, emp2.name, emp2.salary)