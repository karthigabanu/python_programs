import math
class circle:
    def area(self,x):
        self.x=r
        a=math.pi*r*r
        return a
    def perimeter(self,x):
        self.x=r
        b=math.pi*2*r
        return b
r=int(input('enter the radius:'))
obj=circle()
print("area:",obj.area(r))
print("perimeter:",obj.perimeter(r))
