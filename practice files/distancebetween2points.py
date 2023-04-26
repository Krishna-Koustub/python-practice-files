import math 

class distance(object):
    def one_dist(self,x1,y1):
        self.x = x1
        self.y=  y1

    def two_dist(self,x2,y2):
        self.x = x2
        self.y = y2    

x1 =3
y1 =4
x2 =5
y2 =6

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print(result)
