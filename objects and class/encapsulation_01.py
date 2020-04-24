class Computer:
    def __init__(self):
        self.__maxprice = 900
        
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        
    def setMaxPrice(self, price):
        self.__maxprice = price
        
        
comp = Computer()
print("initial sell price")
comp.sell()

print(" ")
#change the price
comp.__maxprice = 1000
print("new price")
comp.sell()

print(" ")
#using setter function
comp.setMaxPrice(1000)
print("using setter to set price")
comp.sell()