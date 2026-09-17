'''
Anonymous function/Lambda Function:
-----------------------------------
-->Anonymous function is a function that don't have any name
--> this alos called as lamba function
-->lamda function will take n number arguments but only one expression

syntax--> lambda arguments : expression

so = lambda a : a+10
print(so(2))

so = lambda a,b,c : a+b+c
print(so(2,24,45))

map():
------
--> the map function will be applied on the given function of each and every element of an itterable

nums=[1,2,3,4,5]
so = list(map(lambda x: x*x,nums))
print(so)
-----------------------------------
filter()
--------
-->filter() function will only consider if the condition is true,then it will keep that values.

nums=[1,2,3,4,5]
so = list(filter(lambda x: x%2==0,nums))
print(so)
------------------------------------
reduce()
--------
-->the reduce() function consider all elements abd reduce to on single element
-->to use this reduce() we have to import it first from the functools.

from functools import reduce
nums = [1,2,3,4,5]
so=reduce(lambda x,y : x+y,nums)
print(so)
-------------------------------------------
print():
--------
-->print() is an in-built function that is used for display the values stored by variable

return():
---------
-->return() only used inside the fucntions
-->when the return is executed then it will exit from that function and holds the returned values in the calling
'''

