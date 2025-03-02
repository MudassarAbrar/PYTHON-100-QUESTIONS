'''
uestion 21
Level 3

Question A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following: UP 5 DOWN 3 
LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps.
Please write a program to compute the distance from current position
after a sequence of movement and original point. If the distance is a 
float, then just print the nearest integer. Example: If the following 
tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, 
the output of the program should be: 2

Hints: In case of input data being supplied to the question, it should
be assumed to be a console input.

'''
import math as m
data = input("ENTER THE DATA: ").split()

def find_distance(data):
    X = 0
    Y = 0
    for x in range(0,len(data),2):
        direction = data[x]
        steps = int(data[x+1])

        if direction == "UP":
            Y += steps
        elif direction == "DOWN":
            Y -= steps
        elif direction == "LEFT":
            X -= steps
        elif direction == "RIGHT":
            X += steps
        
        distance = round(m.sqrt(X**2 + Y**2))
        
    return distance

print(find_distance(data))