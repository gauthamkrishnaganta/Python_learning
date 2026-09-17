'''
Exception Handling:
-------------------
-->An error can be handled by try and except
1.try, 2.except, 3.else, 4.finally

1.try:
------
-->We can the code here which may contain any error

try:
    print(n)
except:
    print('some error')

2.except:
---------
-->exception can handle any error that come in the try block
examples:
try:
    num = 6
    num2 = 0
    print(num/num2)
except:
    print('will get an error')

num = 6
num2 = 0
print(num/num2)
------------------------------
try:
    num = int(input('enter any number: '))
    print(num + 9)
except:
    print('error')
-------------------------------
try:
    print(9 + 'python')
except:
    print('error')
--------------------------------
3.else:
-------
--> if there no error in the code were raised, then the else block will execute
example:
try:
    print(4+5)
except:
    print('error')
else:
    print('no error')
--------------------------
try:
    print('python'+9)
    print('java'+10)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('this will raise zero division error')
except NameError:
    print('this will raise Name Error')
except TypeError:
    print('this will raise Typr Error')
else:
    print('no error')
---------------------------------------
4.finally:
----------
-->it will always executes wheather error is present or not.
examples:
try:
    print('python'+9)
except ZeroDivisionError:
    print('this will raise zero division error')
except NameError:
    print('this will raise Name Error')
except TypeError:
    print('this will raise Typr Error')
else:
    print('no error')
finally:
    print('Thankyou') 
---------------------------------------------------------
try:
    print('Hello')
except ZeroDivisionError:
    print('this will raise zero division error')
except NameError:
    print('this will raise Name Error')
except TypeError:
    print('this will raise Typr Error')
else:
    print('no error')
finally:
    print('Thankyou')
---------------------------------------------------------------
File Handling:
--------------
-->An File Handler is an object used to connect with that particular file
1.with() 2.open()
1.with():
---------
-->by using with keyword no need close the file, it will close it byh itself
syntax:
by file name --> with open('file_name or file_path') as alias_name:
by file path --> with open(r'file_path','mode') as alias_name:
examples:
---------
with open('demo.txt','r') as file:
    print(file.read())
--------------------
with open(r"C:\Users\garap\OneDrive\Documents\Desktop\PFS\Python\demo.txt",'r') as file:
    print(file.read())
------------------------------------------------------------------
2.open():
----------
-->by using open() we have to close the file close().
examples:
---------
any = open('demo.txt','r')
print(any.read())
any.close()
---------------------------------
any = open(r"path",'r')
print(any.read())
any.close()
----------------------------------------------------------------------
Modes:
------
1.'r'
-----
--> the 'r' mode is used for functions read(),readline() and readlines()
example:
--------
with open('demo.txt','w') as file:
    print(file.read())
-------------------------------------------------------
2.'w'
------
-->the 'w' mode is used for write() function
example:
with open("demo.txt",'w') as file:
    file.write('python file handling')
--------------------------------------------------------
3.'a'
-----
-->the 'a' mode is used for write() function and it will add the text at last position
example:
with open('demo.txt','a') as file:
    file.write('\n'+'python error handling')
----------------------------------------------------------
4.'x'
-----
--> the 'x' mode is used to create a file and add the text into it.
example:
--------
with open('demo2.txt','x') as file:
    file.write('python module take 2 hours per day')
-----------------------------------------------------------
functions:
-----------
1.write()
2.read():
---------
-->the read() function will read the file chunk by chunk where we can specify the size
examples:
---------
with open('demo.txt','r') as file:
    print(file.read())
----------------------------
with open('demo.txt','r') as file:
    print(file.read(10))
-------------------------------
3.readline():
-------------
-->it will read only one line at a time
examples:
with open('demo.txt','r') as file:
    print(file.readline())
----------------------------------
4.readlines()
-------------
-->the readlines() will read entire file and writen it in a list, where each line is one
example:
with open('demo.txt','r') as file:
    print(file.readlines())
'''


