from features import Account

wallet = Account(id)

while True:
    id = int(input('Please Enter Your 6-Digit PIN: '))
    trial = 0

    while (id != int(wallet.checkPin()) and trial < 2):
        print('Incorrect PIN. Please Try Again')
        id = int(input('Please Enter Your 6-Digit PIN: '))
        trial += 1

    while trial == 2:
        print('Incorrect PIN Third Times In a Row')
        print('Please Wait For 10 Seconds to Try Again')
        wallet.countDown()
        while id != int(wallet.checkPin()):
            id = int(input('Please Enter Your 6-Digit PIN: '))
        break

    while True:
        print('\t')
        print('Welcome to FundSaver! | Your #1 Digital Wallet Platform')
        print("""
        \t (1) Check Balance
        \t (2) Withdraw
        \t (3) Deposit
        \t (4) Reset PIN
        \t (5) Exit
        """)
        selectMenu = int(input('\nPlease enter the menu number: '))
        if selectMenu == 1:
            print('\nYour Current Balance: Rp ' + str(wallet.checkBalance()) + '\n')

        elif selectMenu == 2:
            nominal = float(input('Enter Balance Amount: '))
            print('CONFIRMATION : You Will Withdraw The Following Amounts. Are You Sure?: y/n'
            + '\n' + str(nominal))
            verifyWithdraw = input('')

            if verifyWithdraw == 'y':
                print('Your Current Balance: Rp ' + str(wallet.checkBalance()) + '')
            else:
                break

            if nominal < wallet.checkBalance():
                wallet.withdrawBalance(nominal)
                print('Withdrawal Success!')
                print('Your Current Balance: Rp ' + str(wallet.checkBalance()) + '')
                print('=================================================================')
            else:
                print('Sorry. You Have Insufficient Balance To Withdraw')
                print('=================================================================')
        elif selectMenu == 3:
            nominal = float(input('Enter Balance Amount: '))
            print('CONFIRMATION : You Will Deposit The Following Amounts. Are You Sure?: y/n'
                  + '\n' + str(nominal))
            verifyDeposit = input('')

            if verifyDeposit == 'y':
                wallet.depositBalance(nominal)
                print('Deposit Success!')
                print('Your Current Balance: Rp ' + str(wallet.checkBalance()) + '')
                print('=================================================================')
            else:
                break

        elif selectMenu == 4:
            verifyPIN = int(input('Please Enter Your Current 6-Digit PIN: '))

            while verifyPIN != int(wallet.checkPin()):
                print('Incorrect PIN. Please Try Again')
                verifyPIN = int(input('Please Enter Your Current 6-Digit PIN: '))

            updatedPIN = int(input('Create Your New 6-Digit PIN: '))
            print('New PIN Assigned!')

            verifyNewPIN = int(input('Please Enter Your New 6-Digit PIN: '))

            if verifyNewPIN == updatedPIN:
                print('PIN Reset Success!')
                print('=================================================================')
            else:
                print('Incorrect PIN. PIN reset failed')
                print('=================================================================')

        elif selectMenu == 5:
            print('Thank You For Choosing FundSaver!')
            print('=================================================================')
            exit()
        else:
            print('Sorry. Menu is not available')
            print('Please choose the available menu')
            print('=================================================================')
