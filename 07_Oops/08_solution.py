class Car:
      total_car = 0
      
      def __init__(self, userbrand, usermodel):
            self.__brand = userbrand
            self.__model = usermodel
            Car.total_car += 1
      def get_brand(self):
            return self.__brand + " !"
            
      def full_name(self):
            return f"{self.__brand} -- {self.__model}"
      
      def fuel_type(self):
            return "Petrol or Diesel"
      
      @staticmethod
      def general_description():
            return "Cars are amazing !"
      @property # This will restrict the user to read only
      def model(self):
            return self.__model
            
my_car = Car("Toyota","Corolla")
# my_car.model = "City"
print(my_car.model)

class ElectricCar(Car):
      def __init__(self, userbrand, usermodel, battery_size):
            super().__init__(userbrand, usermodel)
            
            self.battery_size = battery_size
      def fuel_type(self):
            return "Electric charge"
            
my_batter_car = ElectricCar("Tesla", "Model S", "85kwh")

