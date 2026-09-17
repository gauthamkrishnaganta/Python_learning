'''
Regular Expressions [RegEx]:
----------------------------
--> This RegEx is used to form a searching pattern to find out string contain squence char or not
--> To use this RegEx , we need to import "re" module 

functions:
----------
1.findall:
----------
--> The searching pattern is found, then it will gives the output in the list[]
example:
--------
import re 
some = 'Python is programming language'
print(re.findall('[a]',some))
------------------------------------------
2.search:
---------
--> This is used to forma searching pattern, but it will give only the first matched object.
--> It will gives with the index position , where the matched object is found by pattern.
exaple:
--------
import re
some = 'I have 1000 Rupees'
print(re.search('e',some))
-------------------------------------------
Meta Characters:
----------------
--> Meta Characters are the symbols used in the search pattern.

1.[] 
-----
-->This [] symbol is used to find a group char that present in the string, where we can also specify the range
syntax --> re.findall/search('[range/specific pattern],variable_name')
--> by using this we can search [A-Z], [a-z], [0-9], [some specific pattern]
example:
---------
import re
some = 'We are Going to T20 Match'
print(re.findall('[a-z]',some))
print(re.findall('[aeiou]',some))
print(re.findall('[A-Z]',some))
print(re.findall('[0-9]',some))
-------------------------------------
import re
some = 'We are Going to T20 Match'
print(re.search('[a-z]',some))
print(re.search('[aeiou]',some))
print(re.search('[A-Z]',some))
print(re.search('[0-9]',some))
---------------------------------------
2. . 
-----
--> The dot is a placeholder that can represent any single character, such as a letter, number, or symbol, except a new line.
syntax --> re.search('c..',variable_name)
           re.findall('c...c',variable_name)
example:
--------
import re
name = "My name is prasad"
print(re.findall('p....d',name))
print(re.search('p..',name))
print(re.search('...d',name))
---------------------------------------------
3.^ 
----
--> This symbol is used to find the pattern where string starting match or not
syntax --> re.findall('^',variable_name)
example:
--------
import re
some = 'hello world'
print(re.findall('^he',some))
print(re.search('^he',some))
---------------------------------------------------
4.$
----
--> This symbol will find out if the string is ending with the pattern or not
syntax --> re.findall('sequence$',variable_name)
example:
--------
import re
any = 'I am planning for a trip'
print(re.findall('trip$',any))
print(re.search('trip$',any))
-----------------------------------------------------------
5.{}
-----
--> This symbol is used to find the group of characters that are present in the string
syntax --> re.findall('c.{size}',variable_name)
example:
--------
import re 
all = 'I have 1000 rupees with me'
print(re.findall('I.{5}',all))
------------------------------------------------------------
6.?
----
--> The symbol will find max upto 1 match in the string
syntax --> re.findall('ccc.?',variable_name)
example:
--------
import re
some = 'Hello world!'
print(re.findall('Hell.?',some))
--------------------------------------------------------------
7. *
-----
--> It will find max numkber of sequence from the string
syntax --> re.findall('.*',variable_name)
example:
--------
import re
some = 'Hello world!'
print(re.findall('H.*r',some))
---------------------------------------------------------------
8. +
-----
--> The symbol max number of sequence atleast one character from the starting.
syntax --> re.findall('c.+')
example:
--------
import re
some = 'Hello world!'
print(re.findall('H.+l',some))
---------------------------------------------------------------
check wheather the username is in pattern or not:
-------------------------------------------------
import re
username = input("please enter your name: ")
pattern = re.findall('^[A-Z,a-z]{3,}$',username)
if pattern:
    print('correct unsername')
else:
    print('Incorrect username')
----------------------------------------------------------------- 
'''
