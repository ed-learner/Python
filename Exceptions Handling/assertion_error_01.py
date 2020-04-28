#When an assert statement is encountered, Python evaluates the accompanying expression, 
#which is hopefully true. 
#If the expression is false, Python raises 
#an AssertionError exception.

print("Convert Kelvin to Fahrenheit")
def KelvinToFahrenheit(Temperature):
    assert(Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8) + 32

for i in range(5):
    value = int(input('Enter your input:'))
    test = KelvinToFahrenheit(value)
    print(test)
    
print(" ")   
print("check for division by zero")
value_a = int(input("Enter first value: "))
value_b = int(input("Enter the second value: "))

#using assert to check if second value is 0
assert value_b != 0, "Dividing by 0 error"
print("Values of a/b is: ")
print (value_a / value_b)
