'''
Question 25
Level 1

Question: Define a class, which have a class parameter a
nd have a same instance parameter.

Hints: Define a instance parameter, need add it in init
method You can init a object with 
construct parameter or set the value later
'''
#------------LEVEL 01 QUESTIONS-----------------

class MyClass:
 
    value = "I am a class parameter"

    def __init__(self, value=None):
        # Define an instance parameter
        self.value = value if value is not None else "I am an instance parameter"

# Create an instance of the class
obj = MyClass("Custom instance parameter")

# Access the instance parameter
print("Instance parameter:", obj.value)

# Access the class parameter via the class
print("Class parameter:", MyClass.value)

# Modify the instance parameter
obj.value = "Modified instance parameter"
print("Modified instance parameter:", obj.value)

# Modify the class parameter
MyClass.value = "Modified class parameter"
print("Modified class parameter:", MyClass.value)

# Create another instance and check its parameters
new_obj = MyClass()
print("New object's instance parameter:", new_obj.value)
print("New object's class parameter via class:", MyClass.value)
