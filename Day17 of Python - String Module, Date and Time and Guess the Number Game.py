string Module:
--------------
asscii_letters:
---------------
-->this string module function that can give a-z alphabets
-->upper and lower letters
digits:
-------
-->string module function that can give numbers(0-9)
puntuation:
-----------
-->this string module function can give us
-->puntuation(&$@)

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
------------------------------
creating random password:
-------------------------
import random
import string

letters = string.ascii_letters
digits = string.digits
special_char= '@#$'

all_chars = letters + digits + special_char
password = ''
for i in range(5):
    password += random.choice(all_chars)
print(password)
----------------------------------------------------------------------
Print Date and Time in ATM functions:
-------------------------------------
from datetime import datetime
import sys

bank_bal = 10000
now=datetime.now()

while True:
    print('----------Welcome to SBI ATM-----------')
    user_opt = int(input('1.withdraw /n2.deposite /n3.check balance /n4.exit /nSelect an option: '))
    if user_opt ==1:
        withdraw_m = int(input('enter amount to withdraw: '))
        if withdraw_m < bank_bal:
            bank_bal -= withdraw_m
            print(f'remaining money {bank_bal} {now.strftime("%H:%M , %Y-%m-%d")}')
        else:
            print('insufficient money')

    elif user_opt ==2:
        deposite_m = int(input('enter deposite money: '))
        bank_bal +=deposite_m
        print(f'deposite successfull and total amount {bank_bal}  {now.strftime("%H:%M , %Y-%m-%d")}')
    elif user_opt ==3:
        print(f'avaliable balance:{bank_bal} {now.strftime("%H:%M , %Y-%m-%d")} ')
    elif user_opt ==4:
        sys.exit()
    else:
        print('invalid option')
        print('Thanks for visiting the ATM')
        sys.exit()
-----------------------------------------------------------------------------------------
Game: Guess the Random Number
-----------------------------
import random

ran_num = random.randint(1,100)
guess_num = int(input('Guess the Number [1-100]: '))
if ran_num == guess_num:
    print(f'Your Guess is correct! {ran_num} is the Random number')
else:
    print('incorrect number! better luck next time')
-----------------------------------------------------------------




















