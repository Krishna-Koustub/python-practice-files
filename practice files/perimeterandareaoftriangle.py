class Util:
    def findPerimeter(self, s1, s2, s3):
        return (s1 + s2 + s3)

    def findArea(self, s1, s2, s3):
        p = (s1 + s2 + s3)
        s = p/2
        return (s * (s-s1) * (s-s2)*(s-s3))**0.5


s1 = 3
s2 = 4
s3 = 5

u = Util()

print("The perimeter of the triangle is : {0:.2f}".format(
    u.findPerimeter(s1, s2, s3)))
print("The area of the triangle is : {0:.2f}".format(u.findArea(s1, s2, s3)))