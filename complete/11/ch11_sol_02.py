account_balance = 100000

def check_balance():
    print('계좌금액:', account_balance)

def deposit():
    num = int(input('입금금액:'))
    global account_balance
    account_balance += num
    check_balance()

def withdraw():
    num = int(input('출금금액:'))
    global account_balance
    account_balance -= num
    check_balance()

deposit()
withdraw()



