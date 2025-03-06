'''
Question 56
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
'''

def cal_func(num1,num2):
    try:
        print(num1/num2) 
    except ZeroDivisionError:
        print("Can't divide a number by 0")


cal_func(4,5)
cal_func(5,0)