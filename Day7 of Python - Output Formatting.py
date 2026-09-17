'''
Output Formatting
------------------
1.camma separation(,)

name = 'prasad'
age = 23
print('welcome',name,'your age is',age)
-------------------------------------------
2.F-string (doc-string)

name = 'prasad'
age = 23
print('welcome',name,'your age is',age)
print(f'welcome {name} your age is {age}')
--------------------------------------------
3.Modulo (%)

%d --> digits
%f --> float
%s --> all

name = 'prasad'
age = 23
print('age: %d'%age)

name = 'prasad'
age = 23
print('name: %s'%name)

name = 'prasad'
age = 23
percent = 85.5
print('percentage: %f'%percent)
-----------------------------------
4.Dot format()

name = 'prasad'
age = 23
percent = 85.5
print('name:{}\nage:{}'.format(name,age))
-----------------------------------------
-----------------------------------------
Statements:
------------
there are 3 type of statements.
-->condition
-->control
-->loop
-------------
Condition:
1.if
--> returns the statement if the condition is true.

age = 23
if age >= 18:
    print(f'your age is {age} and eligible to vote')
------------------------------------------------------------
2.if else
--> returns the if block , if condition is true otherwise it returns the else block.

age = int(input('enter your age:'))
if age >= 18:
    print(f'your age is {age} and eligible to vote')
else:
    print(f'your age is {age}, you have to wait {18-age} years')
-------------------------------------------------------------------

example:
To check wheather the given number is even or odd

num = int(input("enter a number:"))
if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")
-------------------------------------------
To check wheather the given alphabet is vowle or consonant

vol = input("enter a sinle Alphabet:")
if vol in "AEIOUaeiou":
    print(f'{vol} is a Vowel')
else:
    print(f"{vol} is a consonant")
---------------------------------------------
To check wheather the given name is palindrome or not

so = input("enter a name:")
if so[::-1] == so:
    print(f'{so} is a palindrome')
else:
    print(f'{so} is a not a palindrome')
---------------------------------------
To check wheather the given year is leap year or not

year = int(input("enter a year:"))
if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
-----------------------------------------


