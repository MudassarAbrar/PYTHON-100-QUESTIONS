'''
Question 96
Please write a program which count and print the numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2 c,2 b,2 e,1 d,1 g,1 f,1

Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.

'''


given_sequence =  input("ENTER THE STRING:  ")


my_dict = {}

for x in given_sequence:
  
    my_dict[x] = my_dict.get(x, 0) + 1

for key, value in my_dict.items():
    print(f"{key},{value}", end=" ")

