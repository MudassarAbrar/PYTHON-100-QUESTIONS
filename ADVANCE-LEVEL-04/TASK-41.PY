'''
Question 41
Define a function which can generate and print a tuple where the value are square of numbers between
1 and 20 (both included).

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values
into a list. Use tuple() to get a tuple from a list.
'''

def tuple_func():
    sqr_list = []
    for x in range(1,21):
        sqr_list.append(x**2)
        
    sqr_tuple = tuple(sqr_list)
    
    print(sqr_tuple)
     
     
tuple_func()