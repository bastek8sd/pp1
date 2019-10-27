login = 'marek'
password = 'm-123'

user_login = input('Podaj login: ')
user_pass = input('Podaj hasło: ')

if user_login == login and user_pass == password:
    print('Poprawne dane')
else:
    print('Podane dane są nieprawidłowe')