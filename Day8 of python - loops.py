elif:
-->elif is short for "else if" and is used to check multiple alternative conditions in a sequential order.
-->if the previous conditions were not true, then try this condition.
-->The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
example:
--------
marks =int(input("enter your marks:"))
if marks >= 90:
    print("A+")
elif marks >= 80:
    print('A')
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C+")
elif marks >= 35:
    print("C")
else:
    print('fail')
----------------------------
To check which is greater value in given values.
num = 89
num2 = 105
num3 = 45
if num > num2 and num > num3:
    print(f'{num} is greater value')
elif num2 > num and num2 > num3:
    print(f'{num2} is greater value')
else:
    print(f'{num3} is greater value')
-----------------------------------
nested if:
-->A nested if statement in Python means placing an if block inside another if, elif, or else block.
-->The inner if condition is evaluated only if the outer condition is true.
-->if statement inside if statement is called nested if statements.
example:
--------
details = {'atmpin':'1811'}
pin = input('enter your 4 digit ATM pin:')
if len(pin) == 4:
    if pin == details['atmpin']:
        opt = int(input('select your option:\n1.Withdraw \n2.Deposit \n3.Pinchange'))
        if opt == 1:
            money_wd = int(input('enter money to withdraw'))
        elif opt == 2:
            money_d = int(input('enter money to deposit'))
    else:
        print('incorrect pin entered')
else:
    print('please enter only 4 digit pin')
-------------------------------------------------------
loops
-----
for loop:
-->for loop is used to itterate over sequence such as str, list, tuple
--> else in for loop will execute when whole itterates are completed.
--> incase if condition becomes true then else will never execute.

eaxmple:
num = [43,67,90,102,57]
for i in num:
    if i == 90:
        continue
    print(i)
else:
    print('end')
-----------------------------------------------
limit_ = int(input('enter the limit:'))
for j in range(1,limit_+1):
    if j % 2 == 0:
        print(f'{j} is even number')
    else:
        print(f'{j} is odd number')
-----------------------------------------------
range():
--> range() is used to generate numbers upto a limit.
syntax--> range(start,end,step)

eaxmple:
for j in range(1,10,2):
    print(j)
----------------------------------------------
To check wheather it is prime or not

num = int(input('enter a number:'))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
    print(f'{num} is prime')
else:
      print(f'{num} is not prime')
----------------------------------
assert keywords:
-->it is keyword used to check the condition.

example:
age = 35
assert age >= 18, 'not eligible'
print('eligible')
--------------------------------


