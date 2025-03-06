'''
Question 42
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

Hints:

Use [n1:n2] notation to get a slice from a tuple.
'''

def tuple_manipulation_func():
    given_tuple = (1,2,3,4,5,6,7,8,9,10)
     
    print(given_tuple[0:len(given_tuple)//2])
    print(given_tuple[len(given_tuple)//2:])
  
    
    
tuple_manipulation_func()