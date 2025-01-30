'''
Question 12
Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''
answers=[]
for x in range(1000,3001,2):
    for y in str(x):
        if int(y)%2!=0:
           break#if the loop encounters any single odd number it breaks else it adds the entire number in the answer list
    else:
     answers.append(x)
print(answers)