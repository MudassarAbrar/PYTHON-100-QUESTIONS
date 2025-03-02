'''
Question 24
Level 1

Question:

Python has many built-in functions, and 
if you do not know how to use it, you can read document online or 
find some books. But Python has a built-in document function for 
every built-in functions.

Please write a program to print some Python built-in functions 
documents, such as abs(), int(), raw_input()

And add document for your own function Hints: The built-in
document method is doc
'''
#---------------------------level 01 question------------------
print("Documentation for abs():")
print(abs.__doc__)

print("\nDocumentation for int():")
print(int.__doc__)




def my_function(func):
    
    return func.__doc__
    

function_name = input("ENTER THE NAME OF THE FUNCTION ACCURATELY: ")
print(my_function(function_name).__doc__)
