'''
Inheritance:
------------
--> Inheritance is the process of inherite one class into another class.
--> will general inherite from a class is called parent class and using it in another that class is called Child Class.
exmaple:
--------
class company:
    def salary(self):
        print('company salary')

class employee(company):
    def mon_salary(self):
        print('Month salary')
emp_sal = employee()
emp_sal.mon_salary()
emp_sal.salary()
---------------------------------------------------------
Types:
------
1.Single Inheritance 2.Multiple Inheritance 3.Muti-level Inheritance 4.Hierarchical Inheritance 5.Hybrid Inheritance

1.Single Inheritance:
---------------------
-->If one child class inherite from one parent class is called single inheritance.

(parent)    A
            |
            |
            |
(child)     B

exmaple:
--------
class father:
    def land(self):
        print('5 acers of land')

class me(father):
    def flat(self):
        print('2 flats')
all = me()
all.flat()
all.land()
-----------------------------------------------------------------
2.Multiple Inheritance:
-----------------------
-->If one class inherite from more than one parent class is called Multiple Inheritance.

(parent)A              B(parent)
         \            / 
          \          /
           \        /
            \      /
             \    /
              \  /
               \/
               C(child)

example:
--------
class grand_father:
    def land(self):
        print('5 acers of land')

class father:
    def home(self):
        print('2 Homes')
class son(grand_father,father):
    def flat(self):
        print('car')

prop = son()
prop.flat()
prop.home()
prop.land()
---------------------------------------------------------------------
Multi-Level Inheritance:
------------------------
-->If one child class become parent class to the another class is called Multi-Level Inheritance.

(grand parent)    A
            |
            |
            |
(parent)B
            |
            |
            |
(child)     C

example:
--------
class grand_father:
    def land(self):
        print('5 acers of land')

class father(grand_father):
    def home(self):
        print('2 Homes')
class son(father):
    def flat(self):
        print('car')

prop = son()
prop.flat()
prop.home()
prop.land()
--------------------------------------------------------------
4.Hierarchical Inheritance:
---------------------------
-->If two child classes inherite from one parent class is called hierarchical Inheritance.

               (parent)A
                   /\
                  /  \
                 /    \
                /      \
               /        \
      (child1)B          C(child2)

example:
--------
class father:
    def land(self):
        print('10 acers land')

class son1(father):
    def flat(self):
        print('son1 flat')

class son2(father):
    def car(self):
        print('son2 car')

s1 = son1()
s1.flat()
s1.land()

s2 = son2()
s2.car()
s2.land()
------------------------------------------------------------------
5.Hybrid Inheritance:
---------------------
--> Inherite from more than two types into one class is called as Hybrid Inheritance.

(parent)    A                                     C(grand parent)
            |                                     |     
            |                                     |
            |                                     |
(child)     B                                     D(parent)
            |                                     |
            |                                     |
            |                                     |
            |                                     E(child)
            |                                     |
            ---------------------------------------
                              |
                              |
                            F(new child)

example:
--------
class person:
    def name(self):
        print('my name is prasad')

class student(person):
    def study(self):
        print('MCA final semester')

class py_teacher:
    def teach(self):
        print('Python')

class J_teacher:
    def teaches(self):
        print('Java')

class learner(py_teacher,J_teacher):
    def learn(self):
        print('Learning')

class get_all(student,learner):
    def get(self):
        print('This person getting all data')

all = get_all()
all.name()
all.study()
all.teach()
all.teaches()
all.learn()
all.get()
--------------------------------------------------------------------------
'''