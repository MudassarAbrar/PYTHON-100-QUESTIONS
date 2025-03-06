'''

Question 92
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints: Use list's remove method to delete a value.

'''


data =  [12,24,35,24,88,120,155]

new_list = [x for x in data if x!=24]

print(new_list)



#==-------------according to questions statement


data = [12, 24, 35, 24, 88, 120, 155]
data.remove(24)
print(data)

