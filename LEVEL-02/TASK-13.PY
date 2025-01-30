'''
Question 13
Level 2

Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following 
input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''
user_input=input("ENTER THE SEQUENCE: ")
digit_count=0
alpha_count=0
for x in user_input:
    if x.isdigit():
        digit_count+=1
    elif x.isalpha():
        alpha_count+=1
    else:
        pass
print(f"ALPHABETS ARE {alpha_count} AND DIGIT COUNT IS {digit_count}")
