'''
Question 76
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints: Use random.choice() to a random element from a list.
'''

import random


even_numbers = [x for x in range(0, 11) if x % 2 == 0]

random_even_number = random.choice(even_numbers)

print("Random even number between 0 and 10:", random_even_number)
