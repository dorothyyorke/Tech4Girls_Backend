class Car:
  def __init__(self, make, model, year): # Constructor (initializer)
    self.make = make
    self.model = model
    self.year = year
  def display_info(self):
    print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info() # Output: Make: Toyota, Model: Camry, Year: 2020