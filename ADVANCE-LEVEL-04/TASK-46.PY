'''
Question 46
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints Use map() to generate a list. Use lambda to define anonymous functions.
'''

def sqr_func():
    num_list = [1,2,3,4,5,6,7,8,9,10]
    
    square_list = map(lambda x : x**2 , num_list)
    
    print(list(square_list))
    
    
    
sqr_func()