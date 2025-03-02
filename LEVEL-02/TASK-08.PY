'''
Question 8
Level 2

Question: Write a program that accepts a comma separated sequence of words as
input and prints the words in a comma-separated sequence after sorting them 
alphabetically. Suppose the following input is supplied to the program:
without,hello,bag,world Then, the output should be: bag,hello,without,world

Hints: In case of input data being supplied to the question, it should be
assumed to be a console input.
'''
#-----------------------with sort fucntion--------------
string_of_words = input("ENTER THE COMMA SEPERATED LIST OF WORDS:  ").split(",")

(string_of_words).sort()

print(string_of_words)
 
#------------------without sort function
def bubble_sort(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:  # Compare adjacent elements
                words[j], words[j + 1] = words[j + 1], words[j]  # Swap
    return words

print(bubble_sort(string_of_words))