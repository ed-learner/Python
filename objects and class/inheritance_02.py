class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputsides(self):
        self.sides = [float(input("Enter side " + str(i+1)+" : ")) for i in range(self.n)]
        
    def dispsides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
        
    def findArea(self):
        a, b, c = self.sides
        
        #calculate the semi-perimeter
        s = (a + b + c)/ 2
        area = (s* (s-a) *(s-b)*(s-c))**0.5
        print('Area of the triangle is %0.2f' %area)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
        
    def findArea(self):
        h, b= self.sides
        area = b*h
        print("Area of the rectangle is %0.2f" %area)
        

print("Triangle")        
tri = Triangle()
tri.inputsides() 
tri.dispsides()
tri.findArea()

print("")
print("Rectangle")
rect = Rectangle()
rect.inputsides()
rect.dispsides()
rect.findArea()