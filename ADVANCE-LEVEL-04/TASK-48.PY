'''
Question 48
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list. Use lambda to define anonymous functions.
'''

def even_func():
    numbers = range(1,21)
    even_numbers = filter(lambda x : x%2 == 0, numbers)
    return list(even_numbers)

print(even_func())