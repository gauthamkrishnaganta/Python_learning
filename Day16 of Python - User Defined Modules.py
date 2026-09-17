'''
User-defined Module:
--------------------
-->user defined modules are created by the programmer. 

syntax --> import module_name

importing with alias name:
--------------------------
--> we can also import a module with different name
--> after importing with the alias name,we have to use that alias name in the code.

example:
import new as cal

print(cal.add(10,20))
print(cal.sub(10,20))
print(cal.mul(10,20))
print(new.add(10,20)) #error - NameError: name 'new' is not defined
---------------
import new
new.display()
---------------------------------------------------------------------
Importing only needed functions:
--------------------------------
--> when we are importing the few functions from the module can only access that functions
syntax--> from module_name import function_names
example:
from new import add

print(add(18,17))
print(sub(23-45))   #error - NameError: name 'sub' is not defined.
-------------------------------------------------------------------------------
Importing all functions:
------------------------
-->use the all functions in that module we have to use (*) to get all of those
syntax--> from module_name import*
example:
--------
from new import*
print(add(10,63))
print(sub(10,63))
print(mul(10,63))
'''
