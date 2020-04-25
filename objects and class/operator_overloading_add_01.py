class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return"({0},{1})".format(self.x, self.y)
        
        
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        
        return Point(x,y)

first_point = Point(2,3)
second_point = Point(4,5)

print(" ")
print("Adding two points:")
print("First point :", first_point)
print("Second point :", second_point)
print("Sum of the two points is:", first_point + second_point)