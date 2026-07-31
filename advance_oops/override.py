class Vehicle:

    def start(self):
        print("Vehicle starts")

class Car(Vehicle):

    def start(self):
        print("Car starts with key")

class ElectricCar(Vehicle):

    def start(self):
        print("Electric car starts with button")

car = Car()
electric = ElectricCar()

car.start()
electric.start()