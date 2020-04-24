
class Parrot:
    #class attribute (characteristics)
    species = "bird"
    
    #instance attribute (characteristics)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#instantiate the Parrot class
Noisy = Parrot("Noisy", 10)
Silent = Parrot("Silent", 15)
 
#access the class attributes
#access the class attribute using __class __.species

print("Noisy is a {}".format(Noisy.__class__.species))
print("Silent is also a {}".format(Silent.__class__.species))
 
 
#access the instance attributes
#ccess the instance attributes using parrot1.name and parrot2.age
print("{} is {} years old".format(Noisy.name, Noisy.age))
print("{} is {} years old".format(Silent.name, Silent.age))