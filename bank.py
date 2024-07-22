def show_balance():
  print(f'Total Blance: ${balance}')

def deposit():
  global balance
  amount = float(input('enter deposit amount:'))
  balance += amount
  print('Deposited')

def withdrawl():
  global balance
  amount = float(input('enter withdrawl amount:'))
  if amount <= balance:
    balance -= amount
    print('Withdrawl succesful')
  else:
    print('Insufficirnt blance.')

balance = 0

while True:
    print('************************')
    print('    Banking Program     ')
    print('************************')
    print('1. Blance')
    print('2. deposit')
    print('3. withdraw')
    print('4. Exit')

    print('************************')
    option = int(input('choose option:'))
    print('************************')
    print('')

    if option == 1:
      show_balance()
    elif option == 2:
      deposit()
    elif option == 3:
      withdrawl()
    elif option == 4:
      print('Done. Thanks for visit')
      break
    else:
      print('Invalid choice.Try again')
