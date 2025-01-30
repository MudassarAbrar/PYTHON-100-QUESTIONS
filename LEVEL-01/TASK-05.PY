'''
Level 1

Question: Define a class which has at least two methods: getString: to get a string from console input 
printString: to print the string in upper case. Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters

'''
class string01play:
    def __init__(self):#constructor
        self.string=""#initializing the string as an empty string
    def getstring(self):
        self.string=input("ENTER THE STRING")
    def printstring(self):
        print(self.string.upper())
sm=string01play()#object of the class
sm.getstring()
sm.printstring()





        

