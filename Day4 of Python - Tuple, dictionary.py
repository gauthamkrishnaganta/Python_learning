'''
Tuple
-->Tuple is collection of different datatype that are repreented in () and separated by ,
-->Tuple is immuttable

methods of Tuple
--------------------
1.index()
syntax--> variable_name.index(item)
example
text = (1, 'java', [3,4], ('python', 78))
print(text.count('python')) --> o/p-->0
print(text.count('python',78)) --> o/p-->1
------------
2.count()
syntax--> variable_name.count(item)
example
any = (1, 'python', (2,['python',9],4),'java', ('python',[56,78],'java',90))
print(any.index('java'))
print(any.count('java'))
-----------------
dictionary:
---------
-->dict is a key:value pair
-->keys and values are separated by :
-->dict is represented by {}
-->keys must be immuttable datatypes
syntax--> variable_name = {key:value}

methods
------
1.keys()
-->syntax-->dict.keys()
----------
2.values()
-->syntax-->dict.values()
-----------
3.items()
-->syntax-->dict.items()
-------
4.update()
-->this method is used to add key:value pair and update the value of any existing pair 
syntax--> dict.update({'key':'value'})
------
5.clear()
-->used to clear all the pairs in a dict
syntax-->dict.clear()
-----------------
example for Dict methods:

details = { 'name':'prasad',
            'acc no':87126392,
            'pan':832648,
            'pin':1234 }
print(details.keys())
print(details.values())
print(details.items())
details.update({'name':'prasad gara'})
print(details)
details.update({'gender':'male'})
print(details)
'''
details = { 'name':'prasad',
            'acc no':87126392,
            'pan':832648,
            'pin':1234 }
print(details.keys())
print(details.values())
print(details.items())
details.update({'name':'prasad gara'})  #updates the value of an existing key
print(details)
details.update({'gender':'male'})       #add the new key:value pair
print(details)
details.clear()
print(details)
