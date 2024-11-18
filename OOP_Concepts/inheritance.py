class Employee:
  def __init__(self, name, position):
    self.name = name
    self.position = position
  def get_details(self):
    print(f"Name: {self.name}, Position: {self.position}")
class Manager(Employee): # Manager inherits from Employee
  def __init__(self, name, position, department):
    super().__init__(name, position) # Use super() to call parent's __init__
    self.department = department
  def get_details(self):
    super().get_details() # Call parent's get_details()
    print(f"Name: {self.name}, Position: {self.position}, Department: {self.department}")
emp = Employee("Bob", "Software Engineer")
emp.get_details()
mgr = Manager("Alice", "Project Manager", "IT")
mgr.get_details()