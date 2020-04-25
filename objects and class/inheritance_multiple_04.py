class Parent:
    def __init__(self):
        self.parentname = "Parent"
        print("Parent properties")
        
class Child:
    def __init__(self):
        self.childname = "son"
        print("Child properties")
        
# We specify all parent classes as 
# comma separated list in bracket.
class grandchild(Parent, Child):
    def __init__(self):
        # calling constructors of parent
        # and child
        Parent.__init__(self)
        Child.__init__(self)
        print("Grand child has properties of both the child and the parent")
        
    def print_hierachy(self):
        print(self.parentname, self.childname)
        
#see the results
print(" ")
print("Lets see what the grandchild has, shall we?")
output = grandchild()
output.print_hierachy