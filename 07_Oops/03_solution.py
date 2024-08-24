class Car:
      def __init__(self, userbrand, usermodel):
            self.brand = userbrand
            self.model = usermodel
            
      def full_name(self):
            return f"{self.brand} -- {self.model}"
      
my_car = Car("Toyota","Corolla")

print("Full details : ", my_car.full_name())


class ElectricCar(Car):
      def __init__(self, userbrand, usermodel, battery_size):
            super().__init__(userbrand, usermodel)
            
            self.battery_size = battery_size
            
my_batter_car = ElectricCar("Tesla", "Model S", "85kwh")

print(my_batter_car.model)            
print(my_batter_car.full_name())            