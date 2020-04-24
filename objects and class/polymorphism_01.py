class Parrot:
    def fly(self):
        print("Parrots can fly")
    def swim(self):
        print("Parrots can not swim")
        
        
class Penguin:
    def fly(self):
        print("Penguin can not fly")
        
    def swim(self):
        print("Penguins can swim!")
        
#common interface for the birds

def flying_test(bird):
    bird.fly()

def swimming_test(bird):
    bird.swim()
    
#instantiate objects
parrot = Parrot()
pingu = Penguin()

print("flying test")
#passing the object
flying_test(parrot)
flying_test(pingu)
print(" ")

print("swiming test")
swimming_test(parrot)
swimming_test(pingu)
