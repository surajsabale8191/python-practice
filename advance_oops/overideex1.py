class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def sound(self):
        print("woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")


cow=Cow()
cat=Cat()
dog=Dog()

cow.sound()
cat.sound()
dog.sound()