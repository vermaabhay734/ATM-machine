print("welcome to SBI bank ATM")
restart=('y')
chances = 3
balance = 1000
while chances>0:
    restart=('y')
    pin = int(input("please enter your secret number"))
    if pin == 1234:
        print('you entered your pin correctly\n')
        while restart not in ('n','N','no','NO'):
            print('press 1 for balance enquiry\n')
            print('press 2 for withdrawl\n')
            print('press 3 for credit money\n')
            print('press 4 for cancel the transaction\n')
            option = int(input("enter your choice\n"))
            if option == 1:
                print('your balance is = ',balance)
                restart = input('would you like to go back?\n')
                if restart in ('n','N','no','NO'):
                    print("thank you")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input("enter the amount for withdrawl = \n"))
                if withdrawl in [100,200,500,1000,]:
                    balance=balance-withdrawl
                    print("your balance is now Rs",balance)
                    restart=input('would you like to restart\n')
                    if restart in ['n','no','N','NO']:
                        print('thank you')
                        break
                elif withdrawl != [100,200,500,1000,]:
                    print('invalid amount! please re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl=float(input('please enter desired amount\n'))

            elif option == 3:
                credit = float(input('enter money which you want to add\n'))
                balance = balance+credit
                print('your balance is = ',balance)
                restart = input('would you like to go back\n')
                if restart in ['n','no','NO','N']:
                    print('thank you')
                    break
            elif option == 4:
                print("your transaction is cancelled")
                print('thank you for your service')
                break
            else:
                print("please enter a correct number\n")
                restart = ('y')
    elif pin != ('1234'):
        print("incorrect password\n")
        chances=chances-1
        if chances == 0:
            print('no more try\n')
            break
