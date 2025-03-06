'''
Question 74
Please generate a random float where the value is between 10 and 100 using Python math module.

Hints: Use random.random() to generate a random float in [0,1].
'''

import random as r

def random_float_generator():
    return f"{round(r.uniform(10,100),2)}, {round(r.random(),2)}"
#the first one creates a random float in the given range while the second one creates the randm float between 0.0 and 1.0
print(random_float_generator())