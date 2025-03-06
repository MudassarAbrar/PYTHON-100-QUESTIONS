'''
Question 31
Define a function that can accept two strings
as input and print the string with maximum length
in console. If two strings have the same length, 
then the function should print al l strings line by 
line.

Hints:

Use len() function to get the length of a string
'''
def max_len_func(str1, str2):
    return(
        str1 if len(str1) > len(str2) 
        else str2 if len(str1) < len(str2)
        else (str1, str2)
        )
    
    
print(max_len_func("HELLOW","WORLD"))