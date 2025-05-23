# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car 
# class during initialization. Access a method of the Engine class via the Car class.



class Engine:
    def start(self):
        print("Engine started")
        


class Car:
    def __init__(self):
        self.engine = Engine()  #car has an engine object (composition)
        self.engine.start()
        print("Car is moving")



car = Car()
        