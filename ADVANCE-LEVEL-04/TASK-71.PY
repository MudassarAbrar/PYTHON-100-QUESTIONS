'''
Question 71
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints: Use eval() to evaluate an expression.
'''
#eval() takes the string and interprets it as Python code.
def evaluation(expression:str):
    print(eval(expression))
    
    
evaluation("35+3")