class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  @property
  def area(self):
    return self.length * self.width
  @property
  def perimeter(self):
    return 2 * (self.length + self.width)
  def __str__(self): # dunder method for string representation
    return f"Rectangle(Length: {self.length}, Width: {self.width})"
  def __eq__(self, other): # dunder method for comparison
    return self.area == other.area
rect1 = Rectangle(5, 3)
rect2 = Rectangle(2, 7.5) # different dimensions
print(rect1) # Output: Rectangle(Length: 5, Width: 3)
print(f"Area of rect1: {rect1.area}") # Output: Area of rect1: 15
print(f"Perimeter of rect1: {rect1.perimeter}") # Output: Perimeter of rect1: 16
print(rect1 == rect2) # Output: True (because areas are equal: 15)
