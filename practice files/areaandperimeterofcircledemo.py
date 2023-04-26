class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * (self.radius ** 2)
    def circumference(self):
        return 2 * 3.14 * (self.radius) 

r =  int(input("Enter the radius: "))        
obj =Circle(r)

print("Area of circle:",obj.area())
print("Circumference of circle:",obj.circumference())