'''
constructor:
-----------
--> __init__
--> the constructor is a special method that only run when the object is created
--> mostly we will take data inside this method
self:
-----
-->the self keyword reffers to current object
example:
--------
class stu:
    def __init__(self):
        self.name = 'prasad'

    def any(self):
        print(self.name)

s1 = stu()
s1.any()
------------------------
class stu_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age

    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')

data1 = stu_data('sony',125,34)
data1.student()
-----------------------
Encapsulation:
--------------
--> Wrapping data and method together is called as encapsulation and using or controlling the data in methods
example:
--------
class stu_data:
    def __init__(self,name,batch,age,fee):
        self.name = name
        self.batch = batch
        self.age = age
        self._fee = fee

    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age} and fee {self.fee}')

data1 = stu_data('sony',125,34,10000)
data1.student()
----------------------------------------------------
Access specifiers:
------------------
1.public (name):
----------------
-->this can be access normally and can call it like a normal variable
eg:
self.name = name
print(self.name)
----------------------------------------------------
2.protected (_name):
--------------------
--> just addinhg single underscore(_) before a varibale it becomes protected variable
eg:
self._age = age
print(self._age)
-----------------
example:
class stu_data:
    def __init__(self,name,batch,age,fee):
        self._name = name
        self._batch = batch
        self._age = age
        self._fee = fee

    def only_name(self):
        print(f"{self._name}")

    def only_batch(self):
        print(f"{self._batch}")

    def only_age(self):
        print(f"{self._age}")

    def only_fee(self):
        print(f"{self._fee}")

data1 = stu_data('sony',125,34,45000)
data1.only_name()
data1.only_batch()
data1.only_age()
data1.only_fee()
---------------------------------------------------------
3.private (__name):
-------------------
-->Adding double underscores (__) before a variable it becomes private variable
eg:
self.__balance = balance
print(self.__balance)
------------------------------
class bank_ac:
    def __init__(self):
        self.name = 'prasad'
        self.adr = '123456789'
        self.pan = 'JGLPD1234F'
        self.__balance = 45000


    def details(self):
        print(self.name)
        print(self.adr)
        print(self.pan)

    def bank_bal(self):
        print(self.balance)

AC = bank_ac()
AC.details()
---------------------------------
class employee:
    def __init__(self):
        self._name = 'prasad'
        self.role = 'web developer'
        self.__salary = '100000'
        self._experience = 5
        self._emptype = 'full-time'

    def details(self):
        print(self.name)
        print(self.role)

    def income(self):
        print(self.__salary)

    def type(self):
        print(self._experience)
        print(self._emptype)

emp = employee()
emp.details()
emp.income()
emp.type()
--------------------------------------
class university:
    def __init__(self,name,course,fee):
        self._name = name
        self._course = course
        self._fee = fee

    def only_name(self):
        print(f"{self._name}")

    def only_course(self):
        print(f"{self._course}")

    def only_fee(self):
        print(f"{self._fee}")

data1 = university('AU','MCA',15000)
data1.only_name()
data1.only_course()
data1.only_fee()
-------------------------------------
'''




















