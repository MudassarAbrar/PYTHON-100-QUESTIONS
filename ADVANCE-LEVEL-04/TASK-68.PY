'''
Question 68
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints: Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def even_num_generator(n):
    even_num = []
    for x in range(n+1):
        if x%2==0:
            even_num.append(x)
            
    print(",".join(map(str,(even_num))))
    
    
    
even_num_generator(10)