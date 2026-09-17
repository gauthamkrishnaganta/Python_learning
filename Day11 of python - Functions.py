'''
Functions
----------
-->Functions is block of code that will be executed when we call it.
--> It is used to avoid the repeated lines of code.
Syntax--> def function_name(parameters):
              ------------
              ------------
              ------------
          function_name(arguments)
--> there are 2 type of functions:
1.Build-in -->print(),len(),max(),min()
2.User defined:
-->User-defined are the functions that are develop by the user.

examples:
num = 10
num2 = 20
def total(num,num2):
    print(num + num2)
total(num,num2)
total(10,30)
total(2,5)
          
def sub(num,num2):
    print(num - num2)
sub(num,num2)
sub(100,30)
sub(20,15)
-------------------------------------------
Required Arguments:
---------------------
-->We have to pass same number of arguments that match in the parameters

example:
num = 10
num2 = 20
def total(num,num2):
    print(num + num2)
total(num,num2)
total(10,30,30)
----------------------------------------
Positional Arguments:
---------------------
-->It does not matter how we are passing the variable,if we assign the value to that variable in the calling

examples:
def name(name='ravi'):
    print(name)
name('prasad')

def name(name2,name1):
    print(name1)
    print(name2)

def pos(m,d,a,c,b):
    print(a)
pos(a=0,b=8,c=4,d=1,m=7)
-------------------------------------------------
Default arguments:
------------------
-->Default arguments in Python are parameters that automatically assume a predefined fallback value if no value is provided for them during a function call.

examples:
def any(age,edu,name):
    print(age)
any('prasad',23,'MCA')

def any(age,edu,name):
    print(age)
any(name='prasad',age=23,edu='MCA')
--------------------------------------------------
'''
        





