class Parrot:
    #instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #instance method
    #called instance method because they are called on 
    #an instance object 
    def sing(self, song):
        return "{} sing {}".format(self.name,song)
    
    def dance(self):
        return "{} is now dancing ".format(self.name)
    
#instantiate the object
NoisyParrot = Parrot("NoisyParrot", 10)
SilentParrot = Parrot("SilentParrot",20) 

#call our instance methods
print(NoisyParrot.sing("'Happy'"))
print(NoisyParrot.dance())

print(SilentParrot.sing("'Happy happy'"))
print(SilentParrot.dance())