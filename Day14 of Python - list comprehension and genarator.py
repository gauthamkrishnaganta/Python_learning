'''
List Comrehension:
------------------
-->the comprehension is the short form of syntax used to generate a new list from the old list>

syntax-->[expression loop]

nums =[1,2,3,4,5]
new_l=[j if j % 2 == 0 else 'odd' for j in nums]
print(new_l)

nel = [i for i in nums if i % 2 != 0]
print(nel)
---------------------------------------
Nested comprehension:
---------------------
-->Nested comprehension means an comprehension inside the another comprehension is called nested comprehension.

syntax--> [expression loop1 and loop2]

match = [[1,2,3],[4,5,6],[7,8,9]]
any=[i for i in match]
print(any)
all=[num for j in match for num in j]
print(all)
--------------------------------------
How to Create Nested Comprehension:

new =[[i*j for j in range(1,6)] for i in range(1,6)]
ne = [i for i in range(1,6)]
print(ne)
print(new)
--------------------------------------
Generator:
----------
--> This generator will generate value one at a time and pause it on the same position when we are using yield() keyword.
--> here we will use 'yeild()' to get the value

syntax--> def function_name(start,step,end)
yield keyword:
--------------
--> this yield() is used to get the value and will only gives one value and pauses there itself.

next keyword:
-------------
--> the next() will retrieve the value

def gen(n):
    for i in range(1,n+1):
        yield i*i
a = gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


'''

