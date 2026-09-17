SBI_ACC = {'name':'prasad',
           'adr':'92739719',
           'pan':'81298',
           'ATMPIN':'1811',
           'balance':5000,
           'transactions':[]}
remain_atp = 3
while remain_atp > 0:
    pin = input('enter your 4 digit pin: ')
    if len(pin) == 4:
        if pin in SBI_ACC['ATMPIN']:
            opt = int(input('1.Withdraw \n2.Deposite \n3.Balance \n4.Transactions \n5.Pin change \nselect a option: '))
            if opt ==1:
                withdraw_a = int(input('enter withdrawal amount: '))
                if withdraw_a <= SBI_ACC['balance'] and withdraw_a % 100 ==0:
                    SBI_ACC['balance'] -= withdraw_a
                    print(f'you have withdraw {withdraw_a} and the remaining balance is {SBI_ACC["balance"]}')
                    SBI_ACC['transactions'].append(f'withdraw - {withdraw_a}')
                    user = int(input('1.Home page \n2.Exit \nselect option: '))
                    if user == 1:
                        print('Home page')
                    else:
                        print('Thankyou')
                        break
                else:
                    print('can not provide change or No sufficiant balance')
                    break        
            elif opt ==2:
                deposite_a = int(input('enter deposite amount: '))
                if deposite_a % 100 == 0:
                    SBI_ACC['balance'] += deposite_a
                    print(f'you have deposited {deposite_a} and the total amount is {SBI_ACC["balance"]}')
                    SBI_ACC['transactions'].append(f'Deposite + {deposite_a}')
                    user = int(input('1.Home page \n2.Exit \nselect option: '))
                    if user == 1:
                        print('Home page')
                    else:
                        print('Thankyou! visit again')
                        break
                else:
                    print('change can not be deposited')                
            elif opt ==3:
                print(f'your account balance is {SBI_ACC["balance"]}')
                user = int(input('1.Home page \n2.Exit \nselect option: '))
                if user == 1:
                    print('Home page')
                else:
                    print('Thankyou! visit again')
                    break 
            elif opt == 4:
                for i in SBI_ACC['transactions']:
                    print(i)
                user = int(input('1.Home page \n2.Exit \nselect option: '))
                if user == 1:
                    print('Home page')
                else:
                    print('Thankyou! visit again')
                    break
            elif opt == 5:
                old_pin= input('enter old pin: ')
                if old_pin == SBI_ACC['ATMPIN']:
                    new_pin =input('enter new pin: ')
                    if len(new_pin) == 4 and new_pin != SBI_ACC['ATMPIN']:
                        SBI_ACC['ATMPIN'] = new_pin
                        print('pin changed successfully.')
                    else:
                        print('please enter only 4 digit pin and it should not be same as current pin')
                        user = int(input('1.Home page \n2.Exit \nselect option: '))
                        if user == 1:
                            print('Home page')
                        else:
                            print('Thankyou! visit again')
                            break              
                else:
                    print('entered incorrect old pin')              
            else:
                print('choose a valid option')  
        else:
            remain_atp -=1
            if remain_atp > 0:
                print(f'Incorrect pin and you have only {remain_atp}')
            else:
                print('card is block')
                break
    else:
        print('pls enter only 4 digit atm pin')
