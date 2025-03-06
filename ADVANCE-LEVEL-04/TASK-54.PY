'''
Question 54
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
'''

class Shape:
    def __init__(self):
        self.name = "Shape"
        
    def area(self):
        print(f"The area of the {self.name} is 0 ")



class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.name = "Square"
        self.length = length
        
    def area(self):
        return (self.length)*(self.length)
    
    
shape = Shape()

shape.area()


square = Square(5)

print(square.area())