'''
Question 53
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
'''

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        
    def area_of_rectangle(self):
        return f"{(self.length)*(self.width):.2f}"
    
    
    
rect01 = Rectangle(3,4)

print(rect01.area_of_rectangle())