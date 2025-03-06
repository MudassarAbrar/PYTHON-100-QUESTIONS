'''
Question 79
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints: Use random.sample() to generate a list of random values.

'''

import random as r

even_numbers = [x for x in range(100, 201) if x % 2 == 0]


my_list = r.sample(even_numbers, 5)

print(my_list)
