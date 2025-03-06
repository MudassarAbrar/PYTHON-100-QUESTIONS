'''
Question 95
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints: Use Subclass(Parentclass) to define a child class.

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"


class Male(Person):
    def __init__(self, name, age, gender):  
        super().__init__(name, age)
        self.gender = gender

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"


class Female(Person):
    def __init__(self, name, age, gender): 
        super().__init__(name, age) 

    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"


Mudassir = Male("Mudassir Abrar Baig", 19, "Male")  

print(Mudassir)
