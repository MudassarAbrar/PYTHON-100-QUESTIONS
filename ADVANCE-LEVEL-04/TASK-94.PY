'''

Question 94
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints: Use set() to store a number of values without duplicate.

'''



data = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]


new_data = []

for item in data:
    if item not in new_data:
        new_data.append(item)
        
        
print(new_data[: : -1])
