'''
Module:
--------
-->Module are the python code which is saved in (.py) that contains functions,variables,classes

types: Built-in & User-defined
------
1.Built-in
-----------
--> the build-in modules are already designed which comes with python when we are installing
eamples:
--------
1.math:
-------
-->math module used to work on matrhematical functionalities.
floor:
------
-->it will round-down to the near value.
ceil:
-----
-->it will round-up to the near value.
import math
print(math.floor(3.78))
print(math.ceil(3.78))
-----------------------
gcd:
----
-->it will find GCD value
lcm:
----
-->it will find LCM value
import math
print(math.gcd(24,50))
print(math.lcm(24,50))
-------------------------
sqrt:
-----
-->it will find the square root value
import math
print(math.sqrt(25))
---------------------
factorial:
----------
-->it will find the factorial of a number.
import math
print(math.factorial(5))
-------------------------------------
log & cos:
----------
import math
pirnt(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)
------------------------------------------------------------------
2.sys:
------
-->it is used to get the details of python interpreter.
version:
--------
-->it prints the version of the python interpreter.
import sys
print(sys.version) #it prints the version - 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)]
path:
-----
--> .py path we will get by this function.
import sys
print(sys.path)
exit():
-------
-->this function will exit from the program.
import sys
print(sys.exit())
platform:
---------
-->it will gives the python run platform
import sys
print(sys.platform)
argv:
-----
-->it will give the current file run path
import sys
print(sys.argv)

-----------------------------------------------
3.random:
---------
-->the random module used to get random elements.
randint:
--------
--> used to generate random numbers based on the range.
import random
print(random.randint(1000,9999))    #gives a random number from 1000 to 9999
choice:
-------
-->
import random
color = ['red','pink','black','blue','white']
print(random.choice(color))
shuffle:
---------
-->it can shuffle the data randomly
import random
color = ['red','pink','black','blue','white']
random.shuffle(color)
print(color)
-----------------------------
uniform:
--------
-->it will gives the decimal values in a given range.
import random
print(random.uniform(1,100))
-------------------------------------------------------------------------------
4.datetime:
-----------
-->it will gives the date and time.
strftimr():
-----------
-->strftime() function lets us convert a datetime object into a formatted string using special format codes.
%Y/%y --> year
%m --> month
%d --> date
%A --> day
%B --> month
%H,%M,%s --> hour,mintues,seconds

example:
from datetime import datetime

now = datetime.now()
print(now)
print(datetime.today())
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%y - %m - %d"))
-------------------------------------------------------
'''

