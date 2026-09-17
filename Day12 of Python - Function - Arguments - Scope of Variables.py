'''
variable - length positional arguments:
----------------------------------------
Arbitrary Arguments - *args :
-----------------------------
--> we can pass tuple of arguments and stored in a single parameter by just adding * before the parameter.
--> we can access the arguments using indexing.

def all(*nums):
    print(nums)
all(10,20,30,40)
-------------------------------------------------------
variable - length keyword arguments:
------------------------------------
Arbitrary Keyword Arguments - **kargs:
--------------------------------------
-->By passing keywords arguments in the arguments,will get it as dictionary just adding ** before the parameter
-->can access by using dictionary methods.

def det(**all):
    for key,val in all.items():
        print(key,':',val)
det(name='prasad',age='23',role='trainee')

def det(*args,**kargs):
    print(args)
    print(kargs)
det(12,34,56,name='prasad',age='23',role='trainee')
---------------------------------------------------------
Scope of Variables:
-------------------
Local Variables:
----------------
-->Variables that are created inside of a function are known as local variables.
-->local variables can be used inside of function only.
Gobal Variables:
----------------
-->Variables that are created outside of a function are known as global variables.
-->Global variables can be used by everyone, both inside of functions and outside.
example:
--------
num2 = 20            #Global Variable
def nums(num2):
    num=60           #Local Variable
    print(num)
    print(num2)
nums(num2)
print(num2)

Fibonacci series:
------------------
num =0
num2 = 1
limit = int(input('enter limit: '))
def series(num,num2,limit):
    print(num,num2,end=' ')
    for j in range(1,limit+1):
        all_sum = num + num2
        num = num2
        num2 = all_sum
        print(all_sum,end=' ')
series(num,num2,limit)
-----------------------------------------------------------
passing by values:
------------------
-->passing direct values in the arguments.

def any(a,b):
    print(a)
    print(b)
any(20,30)
---------------------
passing by Refference:
----------------------
-->passing the values through refference

def any(num,num2):
    print(num)
    print(num2)
any(num=45,num2=50)   

'''
