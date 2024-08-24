class Car:
      def __init__(self, userbrand, usermodel): # Constructor
            self.brand = userbrand
            self.model = usermodel
            
      
my_car = Car("Toyota","Corolla") # No linking if 'self' not used
print("Object: ", my_car.brand)
print("Object: ", my_car.model)


my_new_car = Car("Tata", "Safari")
print("Object: ", my_new_car.brand)
print("Object: ", my_new_car.model)