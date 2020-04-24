# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")
        
    def whoisThis(self):
        print("I am a Bird")
        
    def swim(self):
        print("Swim slower")
        
        
#first child class
class Penguin(Bird):
    
    def __init__(self):
        #call super() function to pull the content of __init__() method 
        #from the parent class into the child class.
        super().__init__()
        print("Penguin initilized")
        
    def whoisThis(self):
        print("I am a Penguin")
        
    def run(self):
        print("Run faster penguin")
        
#second child class
class Eagle(Bird):
    def __init__(self):
         #call super() function to pull the content of __init__() method 
        #from the parent class into the child class.
        super().__init__()
        print("Eagle initialized")
        
    def whoisThis(self):
        print("I am an Eagle")
        
    def fly(self):
        print("Fly higher eagle")
        
print("First child")        
pingu = Penguin()
pingu.whoisThis()
pingu.swim()
pingu.run()

print(" ")

print("Second child")
eagle = Eagle()
eagle.whoisThis()
eagle.swim()
eagle.fly()





