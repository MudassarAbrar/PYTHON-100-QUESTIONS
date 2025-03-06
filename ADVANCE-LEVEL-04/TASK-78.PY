'''
Question 78
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints: Use random.sample() to generate a list of random values.

'''
import random as r

my_list = []

for x in range(5):
    my_list.append(r.randint(100,200))
    
    
print(my_list)

my_list = r.sample(range(100, 201), 5)
#r.sample returns a list (list,no.of elements)
print(my_list)
