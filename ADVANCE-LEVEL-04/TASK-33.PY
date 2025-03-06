'''
Question 33
Define a function which can print a dictionary where the keys are numbers 
between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

'''

def dic_fucntion():
  
    square_dict = {}  
    for num in range(1, 4): 
        square_dict[num] = num ** 2  
    print(square_dict)  
    

dic_fucntion()
