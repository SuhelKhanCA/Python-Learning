class Car:
      def __init__(self, userbrand, usermodel):
            self.__brand = userbrand
            self.model = usermodel
      def get_brand(self):
            return self.__brand + " !"
            
      def full_name(self):
            return f"{self.__brand} -- {self.model}"
      def fuel_type(self):
            return "Petrol or Diesel"
            
my_car = Car("Toyota","Corolla")
print(my_car.fuel_type())

class ElectricCar(Car):
      def __init__(self, userbrand, usermodel, battery_size):
            super().__init__(userbrand, usermodel)
            
            self.battery_size = battery_size
      def fuel_type(self):
            return "Electric charge"
            
my_batter_car = ElectricCar("Tesla", "Model S", "85kwh")

print(my_batter_car.fuel_type())  