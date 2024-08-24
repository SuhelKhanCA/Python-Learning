class Car:
      total_car = 0 # class variable
      
      def __init__(self, userbrand, usermodel):
            self.__brand = userbrand
            self.model = usermodel
            Car.total_car += 1
      def get_brand(self):
            return self.__brand + " !"
            
      def full_name(self):
            return f"{self.__brand} -- {self.model}"
      def fuel_type(self):
            return "Petrol or Diesel"
            
my_car = Car("Toyota","Corolla")


class ElectricCar(Car):
      def __init__(self, userbrand, usermodel, battery_size):
            super().__init__(userbrand, usermodel)
            
            self.battery_size = battery_size
      def fuel_type(self):
            return "Electric charge"
            
my_batter_car = ElectricCar("Tesla", "Model S", "85kwh")


print("No of Cars : ", Car.total_car) # Accessing class variable