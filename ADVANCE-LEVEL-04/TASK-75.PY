'''
Please generate a random float where the value is between 5 and 95 using Python math module.

Hints: Use random.random() to generate a random float in [0,1].
'''
import random

# Generate a random float between 5 and 95
random_float = 5 + (random.random() * random.randint(5,95))
print(round(random_float,2))
