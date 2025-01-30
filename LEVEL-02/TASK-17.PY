'''
Question 17
Level 2

Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100
Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''
seq=input("ENTER THE TRANSACTIONS DATA: ")
seq=seq.split()
amount=0
for x in range(0,len(seq)-1,2):
    if seq[x]=="D":
        amount+=int(seq[x+1])
    elif seq[x]=="W":
        amount-=int(seq[x+1])
print(f"Total amount is {amount}")
