'''

Question 99
Please write a program which prints all permutations of [1,2,3]

Hints: Use itertools.permutations() to get permutations of list.


'''
import itertools


data = [1,2,3]

permutation = list(itertools.permutations(data, r=None))


print(permutation)


