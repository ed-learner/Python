class Equalorgreater:
    def __init__(self, value):
        self.value = value
        
    def __greater__(self, other):
        if(self.value < other.value):
            return "First value is less than second"
        else:
            return "Second value is less than first value"
        
    def __equal__(self, other):
        if(self.value == other.value):
            return "Both values are equal"
        
        else:
            return "Both values are not equal"
        
#first = Equalorgreater(4)
#second = Equalorgreater(5)
#print(first < second)

third = Equalorgreater(4)
fourth = Equalorgreater(5)
#print(first==second)
print(fourth==third)
        

