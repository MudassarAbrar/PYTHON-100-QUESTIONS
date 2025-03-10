'''
Question 70
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints: Use "assert expression" to make assertion.
'''


numbers = [2, 4, 6, 8]

for num in numbers:
    assert num % 2 == 0, f"{num} is not an even number"

print("All numbers are even!")
