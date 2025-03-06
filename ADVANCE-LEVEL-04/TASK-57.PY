'''
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.
'''

class ExceptionClass(Exception):
    def __init__(self, message:str):
        self.message = message 
        super().__init__(message) 


try:
    raise ExceptionClass("This is a custom exception message.")
except ExceptionClass as e:
    print(f"Caught an exception: {e.message}")