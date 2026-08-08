#Password security checher

password = input('Enter your password: ')

if len(password) == 0:
    print('Password cannot be empty!')
elif '123' in password or password.isdigit():
    print('Very weak password~')
elif len(password) >= 8 and " " not in password:
    print('Strong password!')
else:
    print('Weak password!')
