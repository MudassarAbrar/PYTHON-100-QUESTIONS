'''
Question 50
Define a class named American which has a static method called printNationality.

Hints: Use @staticmethod decorator to define class static method.
'''


'''
A static method is a method within a class that does not depend on any instance 
or class-level data. Static methods are defined using the @staticmethod decorator.
They can be called directly on the class itself without creating an instance.'''

'''
Use Case
Static methods are useful when you need a method that logically belongs to a class
but does not need to access or modify the class's instance or class variables.
'''
class American:
   
    @staticmethod
    def printNationality():
        print("I am American.")

American.printNationality()

obj = American()
obj.printNationality()
