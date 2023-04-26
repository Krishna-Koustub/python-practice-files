import math 

class distance(object):
    def one_dist(self,x1,y1):
        self.x = x1
        self.y=  y1

    def two_dist(self,x2,y2):
        self.x = x2
        self.y = y2    

x1 =int(input ("value of x1 "))
y1 =int(input ("value of y1 "))
x2 =int(input ("value of x1 "))
y2 =int(input ("value of y2 "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print(result)

