problems on Loops:
-------------------
To generate prime and not prime numbers upto 10

for i in range(2,10+1):
    count = 0
    for j in range(1,i+1):
        if i % j ==0:
            count += 1
    if count == 2:
        print(f'{i} is prime')
    else:
        print(f'{i} is not prime')
------------------------------------------
To check wheather it is palindrome or not

word = input('enter a word:')
emp = ''
for j in word:
    emp = j + emp
if emp == word:
    print(f'{word} is palindrome')
else:
    print(f'{word} is not plaindrome')
-------------------------------------
To Print stars (triangle pattern)

start = int(input('enter a num: '))
for j in range(1,start+1):
    for i in range(1,j+1):
        print('*',end='')
    print()
-------------------------------------
To Print Numbers(triangle pattern)

start = int(input('enter a num: '))
for j in range(1,start+1):
    for i in range(1,j+1):
        print(i,end='')
    print()
-------------------------------------
To Print Continue Numbers(triangle pattern)

count = 0
start = int(input('enter a num: '))
for j in range(1,start+1):
    for i in range(1,j+1):
        count += 1
        print(count,end='')
    print()
---------------------------------------
To Print Stars(Reverse triangle pattern)

start = int(input('enter a num: '))
for j in range(start,0,-1):
    for i in range(1,j+1):
        print('*',end='')
    print()
---------------------------------------
To Print Stars(Pyramid pattern)

num = int(input('enter a num: '))
for j in range(num):
    print(' ' * (num - j - 1),end = '')
    print('* ' * (j + 1))
---------------------------------------
To Print Stars(Reverse Pyramid pattern)

num2 = int(input('enter a num: '))
for j in range(num2,0,-1):
    print(' ' * (num2 - j),end = '')
    print('* ' * j)
---------------------------------------
To remove duplicates in a list

nums = [1,2,2,3,4,5,5,6,7,7,8]
empt =[]
for j in nums:
    if j not in empt:
        empt.append(j)
print(empt)
------------------------------------------
To check wheather it is perfect Number or not

num = int(input('enter a num: '))
per_num = 0
for j in range(1,num):
    if num % j == 0:
        per_num += j
if per_num == num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not a perfect number')
----------------------------------------------
To print the Table for Given number

tab = int(input('enter a num:'))
for j in range(1,11):
    print(f'{tab} X {j} = {tab*j}')
---------------------------------------
To check wheather it is Amstrong Number or not

num = int(input('enter a num:'))
length = len(str(num))
am = 0
for j in str(num):
    am = int(j) ** length + am
if am == num:
    print(f'{num} is amstrong number')
else:
    print(f'{num} is not amstrong number')
---------------------------------------------
To print Fibonacci series

limit = int(input('enter limit: '))
num = 0
num2 = 1
print(num, num2,end=' ')
for j in range(1,limit+1):
    all_ad = num + num2
    num = num2
    num2 = all_ad
    print(all_ad,end=' ')
------------------------------------------
Calculator

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
opt = int(input('1.Add \n2.Sub \n3.Mul \n4.Div \nselect an option:'))
if opt == 1:
    print(num1 + num2)
elif opt == 2:
    print(num1 - num2)
elif opt == 3:
    print(num1 * num2)
elif opt == 4:
    print(num1 / num2)
else:
    print('choose a valid option')
-------------------------------------
















