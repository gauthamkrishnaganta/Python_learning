'''
Pandas:
-------
--> Pandas are python library used to analysis and manipulation on structure data such as tables, csv file\
--> To use pandas we need to import "pandas" module
example
--------
import pandas as pd
data = pd.Series([1,2,3,4,5,6])
print(data)
---------------------------------------------
Functions in Pandas:
--------------------
1.Series:
---------
--> This function is a one - dimentions labeled data structure
--> The right side is the index value which start from 0
--> Left side normal are values 
accessing by index:
-------------------
--> By acccessing with the index value and will get data of that index
example:
--------
import pandas as pd
data = pd.Series([1,2,3,4,5],index=['zero','one','two','three','four'])
print(data)

--> we can convert a normal dictionary into structure data by pandas
example:
--------
import pandas as pd
stu = {'name':'prasad',
       'age':'23',
       'batch':'6'}
det = pd.Series(stu)
print(det)
------------------------------
2.DataFrame
-----------
--> DataFrame is known as 2 dimention labeled data structure in pandas and which contains rows and columns
--> To convert normal dictionary into structured Data
--> In the values we pass list od data 
example:
--------
import pandas as pd
details = {'brand': ['apple','vivo','pixel'],
           'product':['Mobile','Buds','cable'],
           'price':[50000,2000,1000]}
info = pd.DataFrame(details)
print(info)
print(info['price'])
print(info[['brand','price']])
-----------------------------------------------------------
3.Data Cleaning:
-----------------
-->Data Cleaning is the process of finding problem and fixing it to analysis data 
1.Missing values
2.Incorrect data

methods:
--------
1.head():
---------
--> It returns first 5 rows of data.
import pandas as pd
details = {'brand': ['apple','vivo','pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,5000,30000,3000]}
info = pd.DataFrame(details)
print(info)
print(info.head())
--------------------------------
2.tail()
---------
---> It returns last 5 rows of data.
import pandas as pd
details = {'brand': ['apple','vivo','pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,5000,30000,3000]}
info = pd.DataFrame(details)
print(info)
print(info.tail())
-----------------------------------
3.shape
--------
--> it used to find out the no of rows and columns
import pandas as pd
details = {'brand': ['apple','vivo','pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,5000,30000,3000]}
info = pd.DataFrame(details)
print(info)
print(info.tail())
-----------------------------------------
4.info()
---------
-->It returns the information of the data
-->This method will give us total information about data present
import pandas as pd
details = {'brand': ['apple','vivo','pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,5000,30000,3000]}
all = pd.DataFrame(details)
print(all)
print(all.info())
--------------------------------------------
5.isnull()
----------
-->It returns True any null values present in the data.
example:
-----
import pandas as pd
details = {'brand': ['apple','vivo','pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,None,30000,3000]}
all = pd.DataFrame(details)
print(all)
print(all.isnull())
--------------------------------------------
6.dropna()
----------
-->it returns the remaining data after deleting the complete rows which have Null value
example:
--------
import pandas as pd
details = {'brand': ['apple',None,'pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,5000,30000,None]}
all = pd.DataFrame(details)
print(all)
print(all.dropna())
---------------------------------------------
7.sum()
-------
--> Method can find number of null values present in the data.
syntax --> variable_name.isnull().sum()
example:
--------
import pandas as pd
details = {'brand': ['apple',None,'pixel','samsung','nothing','redme'],
           'product':['Mobile','Buds','cable','watch','mobile','powerbank'],
           'price':[50000,2000,1000,5000,30000,None]}
all = pd.DataFrame(details)
print(all)
print(all.isnull().sum())
---------------------------------------------------
8.duplicated()
---------------
--> it returns True if all the values of coloumn are duplicated values
example:
--------
import pandas as pd
details = {'brand': ['apple','apple','pixel','samsung','nothing','redme'],
           'product':['Mobile','Mobile','cable','watch','mobile','powerbank'],
           'price':[50000,50000,1000,5000,30000,2000]}
all = pd.DataFrame(details)
print(all.duplicated())
----------------------------------------------------
9.read_csv()
------------
--> This can read the csv file data
syntax --> pd.read_csv(file_name)
example:
--------
import pandas as pd
data = pd.read_csv('students.csv')
print(data)
print(data.isnull())
print(data.duplicated())
print(data.duplicated().sum())
print(data.dropna())
-----------------------------------------------------
'''
