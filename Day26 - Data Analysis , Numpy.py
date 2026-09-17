'''
Data Analysis:
--------------
--> Data Analysis is the process of collecting, cleaning, transforming, organizing 
and analyzing data to convert into useful information and used for making decisions to get the
better outcome.

library used:
--------------
Numpy
Pandas
Matplotlib
seaborn

Numpy:
------
--> This refers to numerical python
--> It is an python library used for calculations and operations
--> this python library is more faster than the list to perform operations
--> and also supports multi-dimensional arrays
example:
---------
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)
---------------------------
import numpy as np
arr2 = np.array([1,2,3,4,5])
print(arr2.ndim)
arr3 = np.array([[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
])
print(arr3.ndim)
--------------------------------
functions:
----------
ndim:
-----
--> The function is used to find out the dimentions of an array.
syntax --> array.ndim
example:
--------
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)
---------------------------------------
shape:
------
--> The function is used to find the row & col of an array.
syntax--> array.shape
example:
--------
import numpy as np
arr2 = np.array([1,2,3,4,5])
print(arr2.shape)
arr3 = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr3.shape)
-----------------------------------------------
reshape:
--------
--> The function is used to convert one dimension to another, if the elements are there convert into the any dimension.
syntax --> array.reshape(row,col)
example:
--------
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))

arr2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr2.reshape(3,3))
---------------------------------------------------------------
size:
-----
--> The function is used to find out the number of elements present in a array.
syntax --> array.size
example:
---------
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.size)
-----------------------------------------------------------------
arange:
-------
--> The function is used to generate numbers in a sequence upto certain limit and it can be form 1D array
--> This Array can be reshape or convert into 2D array by using reshape
example:
--------
import numpy as np
arr = np.arange(1,10)
print(arr)
print(arr.reshape(3,3))
------------------------------------------------------------------------
Operations:
-----------
--> same as list we can also perfrom some opeartions on arrays.
1.Indexing:
-----------
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[4])
---------------------
2.sciling:
----------
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[2:4])
----------------------
3.sum:
------
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.sum())
------------------------
4.add:
------
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 + arr2)
print(arr1 + 5)
---------------------------
5.sub:
-------
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 - arr2)
print(arr2 - 5)
----------------------------
6.mul:
-------
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 * arr2)
print(arr2 * 5)
---------------------------
7.powers:
---------
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 ** arr2)
print(arr2 ** 5)
------------------------------
8.max():
--------
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1.max())
------------------------------
9.min():
--------
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1.min())
------------------------------
'''
