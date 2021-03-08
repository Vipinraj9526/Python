#create Rectanglr class with atribute lenght and breadth and method to find area and perimeeter.
#Compare two Rectangle object by thier area.

class Rectangle:
  def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
  def area(self):
      return (self.length*self.breadth)
  def perimeter(self):
      return (2*(self.length+self.breadth))

r1=Rectangle(4,5)
r2=Rectangle(9,2)
print("Area of 1st Rectangle:",r1.area())
print("Area of 2nd Rectangle:",r2.area())
print("Perimeter of 1st Rectangle:",r1.perimeter())
print("Perimeter of 2nd Rectangle:",r2.perimeter())
if r1.area()>r2.area():
   print("first area is grater")
else:
    print("second area is grater")


