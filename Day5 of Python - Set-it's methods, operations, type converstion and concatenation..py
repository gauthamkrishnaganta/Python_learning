'''
Set:
----
-->Set is an unordered collection.
-->Set do not allows duplicate values inside it.
-->Set is muttable
-->Set is Represented in {}

do = {1,2,3,4,2}
print(do)  #o/p--> {1,2,3,4}

Creating a empty set:
--------------------
so = set()
print(type(so))  #o/p--> < class 'set' >
--------------------
Set methods:
------------
1.update:
---------
-->use to add new values into set
syntax --> variable_name.update(itterable)

do = {1,2,3}
do.update([5,9])
print(do)
----------------
2.add:
-----
syntax -->variable_name.add(value)

do={1,2,3}
do.add('python')
print(do)
---------------
3.remove:
-------
-->used to delete the value from the set, incase if the value is not present in the set will get the keyerror.
syntax -->variable_name.remove(value)

do={1,2,3,4}
do.remove(4)
print(do)
-----------
4.discard:
--------
-->used to delete the value from the set , but never give any error incase value is not present inside the set.
syntax -->variable_name.discard(value)

do={1,2,3,}
do.discard(4)
print(do)
---------
5.pop():
--------
-->used to delete the value but this pop() will take 0 arguments inside it, it will automatically deleted the first value.
syntax-->variable_name.pop()

do={1,2,3,4}
do.pop()
print(do)
-------------
operations:
------------
union:
-->returns all sets values together but no duplicates

do={1,2,3}
so={3,4,5}
print(do|so)
print(do.union(so))
----------------
intersection:
-->returns common values in both sets

do={1,2,3}
so={3,4,5}
print(do&so)
print(do.intersection(so))
--------------
difference:
-->returns a new set containing the elements that are present in the first set but not in the second set.

do={1,2,3}
so={3,4,5}
print(do-so)
print(do.difference(so))
-------------------
type convertion:
-----------------
1.integer:

int-->string and float

string -->str()

num=9
print(type(num))
so=str(num)
print(type(so))

float -->float()

num=9
print(type(num))
so = float(num)
print(so)
print(type(so))
---------------------
2.float:

float-->int and str

integer-->int()

nums=8.67
print(type(nums))
all_ = int(nums)
print(all_)
print(type(all_))

string-->str()

nums=8.67
print(type(nums))
all_ = str(nums)
print(type(all_))
-----------------------
3.string:
str-->int,float,list and tuple

integer -->int()  #only for integer values, if you gave string then it will throw error.

how = "67 rupp"
print(type(how))
who = int(how)
print(type(who))

how = "67"
print(type(how))
who = int(how)
print(type(who))

float -->float()  #only for integer and float values, if you gave string then it will throw error.

how = "67"
print(type(how))
who = float(how)
print(type(who))

list -->list()

how = "1234"
print(type(how))
who = list(how)
print(who)
print(type(who))

tuple -- >tuple()

how = "1234"
print(type(how))
who = tuple(how)
print(who)
print(type(who))
--------------
list:
------
list-->string and tuple
string -- str()

nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))

tuple  -->tuple()

nums = [1,2,3,4]
print(type(nums))
all_n = tuple(nums)
print(all_n)
print(type(all_n))
-----------------
tuple:
-------
tuple-->list and string
list -- >list()

nums = [1,2,3,4]
print(type(nums))
all_n = list(nums)
print(all_n)
print(type(all_n))

string -->str()

nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(all_n)
print(type(all_n))
------------------
concatenation(+):

num = 8
num_2 = 9
print(num+num_2)  o/p-->17

any_ = 'python is a'
we = ' language'
print(any_ + we)   o/p-->python is a language


nums = [1,2]
all_ = [3,4]
print(nums + all_)   o/p-->[1, 2, 3, 4]

'''

