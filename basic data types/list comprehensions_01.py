# Using List comprehensions 
# for constructing output list 
  

your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

#find even numbers in the list
even = [value for value in your_list if value % 2 == 0]
odd  = [value2 for value2 in your_list if value2 % 2 != 0]

print(" ")
print("Even numbers in your list:", even)
print("Odd numbers in your list: ",odd)

print(" ")
no_square = [value**2 for value in range(1, 11)] 
print("Square of numbers 1 to 10 :", no_square)