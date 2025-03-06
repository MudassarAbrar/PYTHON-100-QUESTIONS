'''
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.'''

class American:
    def hello(self):
        print("WE ARE THE CITIZEN OF AMERICA")




class NewYorker(American):
    def hi(self):
        print("WE LIVE IN NEW YOKR")
        
        


citizen = NewYorker()

citizen.hi()
citizen.hello()