'''
Question 37
Define a function which can generate and print a list where the values are square of
numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list.
'''

def square_func():
    sqaures_list = []
    for x in range(1,21):
        sqaures_list.append(x**2)
        
    print(sqaures_list)
        
square_func()