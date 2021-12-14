import os
from bank_account_variables import money_slips, accounts_list

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# file = open(BASE_PATH + '/_file_test.dat','w') # write
# file.write('school of net111')
# file.write('\n')
# file.write('school of net111')
# file.close()

# file = open(BASE_PATH + '/_file_test.dat','a') # write
# file.write('school of net111')
# file.write('\n')
# file.write('school of net111')
# file.write('\n')
# file.writelines(('aaaaaaaaa\n','wwwwwwwww\n','eeeeeeeeeee\n'))
# file.writelines(['aaaaaaaaa\n','wwwwwwwww\n','eeeeeeeeeee\n'])
# file.close()

# file = open(BASE_PATH + '/_file_test.dat','r') # write
# print(file.read())
# file.close()

# file = open(BASE_PATH + '/_file_test.dat','r') # write
# print(file.read(10))
# print(file.read(10))
# print(file.read(10))
# file.close()

# file = open(BASE_PATH + '/_file_test.dat','r') # write
# print(file.readline())
# print(file.readline(7))
# print(file.readline(14))
# lines = file.readlines()
# file.close()

# for line in lines:
#     print(line)

# file = open(BASE_PATH + '/_file_test.dat','r') # write
# line = file.readline()
# while line:
#     print(line)
#     line = file.readline()
# file.close()

def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)

#20=5;50=5;100=5
def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')

def write_bank_accounts(file):
    for account, account_data in accounts_list.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';',
            '\n'
        ))

def read_money_slips(file):
    line = file.readline()
    while line.find(';') != -1 :
        semicolon_pos = line.find(';')
        money_bill_value = line[0:semicolon_pos]
        set_money_bill_value(money_bill_value)
        if semicolon_pos + 1 == len(line) :
            break
        else :
            line = line[semicolon_pos+1:len(line)]

def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=') # 20=5000
    money_bill = money_bill_value[0:equal_pos] # 20
    count_money_bill_value = len(money_bill_value)
    value = money_bill_value[equal_pos+1:count_money_bill_value] # 5000
    print(money_bill, value)
    money_slips[money_bill] = int(value)

def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)


def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1 :
        semicolon_pos = account_line.find(';')
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        if semicolon_pos + 1 == len(account_line) :
            break
        else :
            account_line = account_line[semicolon_pos+1:len(account_line)]
    add_bank_account(account_data)


def add_bank_account(account_data):
    accounts_list[account_data[0]] = {
        'name':account_data[1],
        'password':account_data[2],
        'value': float(account_data[3]),
        'admin': True if account_data[4] == 'True' else False
    }


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()
    
    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()