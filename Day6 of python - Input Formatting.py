'''
User Inputs - Input Formatting
------------------------------
INT:
-->int(input())
eg:
num = int(input('enter a number:'))
print(num + 1)
------------------------
Sting:
-->intput()

eg:
text =input('enter a name:')
print(type(text))
--------------------------
list:
-->
num = list(map(int,input('enter numbers:').split()))
print(num)

text = input('enter text:').split()
print(text)
--------------------
tuple:

num = tuple(map(int,input('enter nums:').split()))
print(num)

so = tuple(input('enter tuple:').split())
print(so)
-----------------
To take every data type:

data =  eval(input('enter values:'))
print(data)
print(type(data))
--------------------
converting 24H time into 12H time:

time = input('enter 24H clock:')
parts = time.split(':')
hours = int(parts[0])-12
print(hours, ':' , parts[1], 'pm')
----------------------------
'''
            
