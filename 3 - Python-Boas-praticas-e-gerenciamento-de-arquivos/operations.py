import getpass
from bank_account_variables import accounts_list, money_slips


# accounts_list = bank_account_variables.accounts_list
# money_slips = bank_account_variables.money_slips


###################################################################
def do_operation(option_typed, account_auth):
    if option_typed ==    '1':
        show_balance(account_auth)
    elif option_typed == '10' and accounts_list[account_auth]['admin']:
        insert_money_slips()
    if option_typed ==    '2':
        withdraw(account_auth)


###################################################################
def show_balance(account_auth):
    print('Seu saldo é %s' % str(accounts_list[account_auth]['value']))


###################################################################
def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser incluída: ')
    money_slips[money_bill_typed] += int(amount_typed)
    print(money_slips)


###################################################################
def withdraw(account_auth):
    value_typed = input('Digite o valor a ser sacado: ')
    money_slips_user = {}
    value_int = int(value_typed)

    if value_int <= accounts_list[account_auth]['value']:

        if ((value_int // 100) > 0) and (money_slips['100'] >= (value_int // 100)):
            money_slips_user['100'] = value_int // 100
            value_int = value_int - value_int // 100 * 100

        if ((value_int // 50) > 0) and (money_slips['50'] >= (value_int // 50)):
            money_slips_user['50'] = value_int // 50
            value_int = value_int - value_int // 50 * 50

        if ((value_int // 20) > 0) and (money_slips['20'] >= (value_int // 20)):
            money_slips_user['20'] = value_int // 20
            value_int = value_int - value_int // 20 * 20

        if value_int != 0:
            print('O Caixa não tem cédulas disponíveis para este valor')
        else:
            
            for money_bill_user in money_slips_user:
                money_slips[money_bill_user] -= money_slips_user[money_bill_user]
                accounts_list[account_auth]['value'] -= int(money_bill_user) * money_slips_user[money_bill_user]

            print('Pegue as notas: ')
            print(money_slips_user)
            print(money_slips)
            print(accounts_list[account_auth]['value'])
    else:
            print('Saldo indisponível')


###################################################################
def auth_account():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        return account_typed
    else:
        False


###################################################################
def get_menu_options_typed(account_auth):
    print("1 - Saldo")
    print("2 - Saque")
    if accounts_list[account_auth]['admin'] :
        print('10 - Incluir cédulas')
    return input('Escolha uma das opções acima:')

    