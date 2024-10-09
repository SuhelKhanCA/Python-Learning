# instance and class attribute
class Car:
    wheels = 4 # class attribute

    def __init__(self, color):
        self.color = color # instance attribute

car1 = Car("Red")        
car2 = Car("Green")

print(car1.color, car1.wheels)
print(car2.color, car2.wheels)
