'''
To find datatype -- type(variable_name)
To find memory -- id(variable_name)

DataTypes:
----------
int
num = 9

float
num = 8.5

string
-->String is a sequence of char that are inclosed in ( ' ','' '')
-->String is Immutable

String Methods:
-------
replace()
--> used to replace old string with new string
syntax--> variable_name.replace('old_str','new str')
          variable_name.replace('old_str','new str','no.of times')

so = "python is a language"
print(so.replace("python","java"))
print(so) #it prints python is a language because string is immutable.
-------
join()
-->This method is used to add a new char or a new string after every sub-string.
syntax--> 'new_string'.join(variable_name)

so = 'python is a language'
print('-'.join(so))
--------------------
split()
--> this method is used to split the str with existing str.
syntax-->variable_name.split('existing_str')

so = 'python is a language'
print(so.split('is'))
------------------------
index()
-->Index is the position of an element in the sequence (such as str, list or tuple)
syntax-->varibale_name.index('element')

so = 'python is a language'
print(so.index('s'))
------------------------
count()
-->used to return the no of times a specific substring occurs
syntax-->varibale_name.count('sub_str')

so = 'python is a language'
print(so.count('n'))
--------------------------
list
-->list is the collection of different datatypes that are represented in [] and separated by ,
-->List is the muttable data type
syntax-->list_name = [item1,item2,item3]

any = [1, 'python', [2,['python',9],4],'java', ['python',[56,78],'java',90]]
print(any[4][1][0])
-----------------
list Methods:

append()
--> This method is used to add new item into the list and it will add at last index position.
syntax-->list_name.append(new_item)

any = [1,2,3,4,5]
any.append(10)
print(any)
any.append(100)
print(any)
--------------
extend()
-->used to add all elements of another iterable to end of a list
syntax-->list_name.extend('new_iterable')

any = [1,2,3,4,5]
any.append('python')
print(any)
any.extend('python')
print(any)
-----------
remove()
-->this method is used to delete the first occurrence of a specific element , if the element not in the list then it will show error.
syntax-->list_name.remove(element)

any = [1,2,3,4,5]
any.remove(2)
print(any)
------------
pop()
-->used to delete the specific element that based on the index value . if you not mention the index value then it automatically delete the last element in the list
syntax-->list_name.pop(index_value)

any = [1,2,3,4,5]
any.pop(3)  #it will remove the item in 3rd index value element
print(any)
any.pop()   #it will remove the item in last index value element
print(any)
any.pop(20)
print(any) #it will shows an error
-------------------------------
'''
