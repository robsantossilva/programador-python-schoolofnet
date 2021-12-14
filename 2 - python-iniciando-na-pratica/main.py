import getpass
import os
import time

clear_command = 'cls' if os.name == 'nt' else 'clear'

accounts_list = {
  '0001-02':{
    'password':'123456',
    'name':'Fulano de Tal',
    'value':100,
    'admin': False
  },
  '0002-02':{
    'password':'123456',
    'name':'Cicrano da Silva',
    'value':50,
    'admin': False
  },
  '1111-11':{
    'password':'123456',
    'name':'Admin da Silva',
    'value':1000,
    'admin': True
  }
}

money_slips = {
  '100': 5,
  '50': 5,
  '20': 5
}

while True :
  print("****************************************")
  print("*** School of Net - Caixa Eletrônico ***")
  print("****************************************")

  account_typed = input('Digite sua conta: ')
  password_typed = getpass.getpass('Digite sua senha: ')

  if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:

    os.system(clear_command)

    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")

    print("1 - Saldo")
    print("2 - Saque")

    if accounts_list[account_typed]['admin'] :
      print('10 - Incluir cédulas')

    option_typed = input('Escolha uma das opções acima:')
    if option_typed ==  '1':
      #print('Seu saldo é ' + str(accounts_list[account_typed]['value']))
      print('Seu saldo é %s' % str(accounts_list[account_typed]['value']))
    elif option_typed == '10' and accounts_list[account_typed]['admin']:
      amount_typed = input('Digite a quantidade de cédulas: ')
      money_bill_typed = input('Digite a cédula a ser incluída: ')

      #money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
      money_slips[money_bill_typed] += int(amount_typed)
      print(money_slips)
    if option_typed ==  '2':
      value_typed = input('Digite o valor a ser sacado: ')

      money_slips_user = {}
      value_int = int(value_typed)

      if value_int <= accounts_list[account_typed]['value']:

        for money_bill in money_slips:
          if ((value_int // int(money_bill)) > 0) and (money_slips[money_bill] >= (value_int // int(money_bill))):
            money_slips_user[money_bill] = value_int // int(money_bill)
            value_int -= value_int // int(money_bill) * int(money_bill)

        # if ((value_int // 100) > 0) and (money_slips['100'] >= (value_int // 100)):
        #   money_slips_user['100'] = value_int // 100
        #   value_int = value_int - value_int // 100 * 100

        # if ((value_int // 50) > 0) and (money_slips['50'] >= (value_int // 50)):
        #   money_slips_user['50'] = value_int // 50
        #   value_int = value_int - value_int // 50 * 50

        # if ((value_int // 20) > 0) and (money_slips['20'] >= (value_int // 20)):
        #   money_slips_user['20'] = value_int // 20
        #   value_int = value_int - value_int // 20 * 20

        if value_int != 0:
          print('O Caixa não tem cédulas disponíveis para este valor')
        else:
          
          for money_bill_user in money_slips_user:
            money_slips[money_bill_user] -= money_slips_user[money_bill_user]
            accounts_list[account_typed]['value'] -= int(money_bill_user) * money_slips_user[money_bill_user]

          print('Pegue as notas: ')
          print(money_slips_user)
          print(money_slips)
          print(accounts_list[account_typed]['value'])

      else:
        print('Saldo indisponível')

  else:
    print('Invalid account')

  input('Pressione <ENTER> para continuar...')

  os.system(clear_command)