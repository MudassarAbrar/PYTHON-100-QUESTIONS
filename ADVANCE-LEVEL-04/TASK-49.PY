'''
Question 49
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints Use map() to generate a list. Use lambda to define anonymous functions.
'''


def sqr_func():
    numbers = range(1,21)
    sqr_num = list(map(lambda x : x**2  , numbers))
    return sqr_num


print(sqr_func())