'''
Question 30
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings
'''

def concat_func(str1,str2):
  if type(str1)==str and type(str2)==str:
    return str1 + str2

print(concat_func("HELLO","WORLD"))