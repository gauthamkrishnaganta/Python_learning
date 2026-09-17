'''
OOPs:
-----
--> Object oriented programming System
--> OOPs is used to maintain the code structure in object and classes

1.class:
--------
-->class is an blueprint or template to an object
syntax:
-------
class class_name:
    #attribute
    #methods

class stu:
    name = 'prasad'
    age = 23
s1 = stu()
print(s1.name)
print(s1.age)
---------------------------------------------
2.Object:
---------
--> Object is instance of the class 

3.Attributes:
-------------
-->Attribute is the data present in the class or pass to the class
example:
--------
class details:
    def __init__(self):
        self.name = 'prasad'
        self.age = 23
        self.edu = 'MCA'
        self.role = 'student'
person = details()
print(person.name)
print(person.age)
print(person.edu)
print(person.role)

4.Methods:
----------
-->Method is a function that is created inside the class
syntax:
-------
class class_name:
    #attributes
    def fun_name(self):
    #code
obj = class_name()
print(obj.fun_name())

example:
--------
class car:
    def __init__(self):
        self.color = 'red'
        self.seat = 6
        self.brand = 'BMW'
c1 = car()
print(c1.color)



'''
class details:
    def __init__(self):
        self.name = 'prasad'
        self.age = 23
        self.edu = 'MCA'
        self.role = 'student'
person = details()
print(person.name)
print(person.age)
print(person.edu)
print(person.role)