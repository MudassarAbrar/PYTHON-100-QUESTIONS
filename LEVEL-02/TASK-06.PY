
'''
Question 6
Level 2

Question: Write a program that calculates and prints the value according to
the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed 
values of C and H: C is 50. H is 30. D is the variable whose values
should be input to your program in a comma-separated sequence. Example Let us
assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be rounded off to its nearest
value (for example, if the output received is 26.0, it should be printed as 26) In case of
input data being supplied to the question, it should be assumed to be a console input.
'''







import math as m

D = map(int,input("ENTER THE COMMA SEPERATED LIST: ").split(","))
C = 50
H = 30

for x in D:
    Q = (m.sqrt((2*C*x)/H))
    f_Q = round(Q)
    print(f_Q)
