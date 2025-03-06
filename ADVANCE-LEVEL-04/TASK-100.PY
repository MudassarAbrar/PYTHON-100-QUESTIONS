'''

Question 100
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint: Use for loop to iterate all possible solutions.




'''
head = 35
legs = 94

for chickens in range(head+1):
   rabbits = head - chickens

   if 2 * chickens + 4 * rabbits == legs:
       print(f"Chickens: { chickens} , Rabbits: {rabbits}  ")
       break
