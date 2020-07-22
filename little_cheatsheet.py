# l-ctrl + k + c - comment
# l-ctrl + k + u - uncomment
# print('Hello world!')

# zkouska urcitych vestavenych funcki
# veta = 'muj pes je krasnej!'
# veta_upper = veta.upper()
# print(veta.upper())
# print(veta.lower())
# print(veta.capitalize())
# print(veta.count('a'))
# print(veta_upper)

# placeholders
# 3 types...
# 1) print("ddd" + firstname)
# 2) print("ddd {}".format(first_name))
# 3) print(f'Hello, {first_name}')
# first_name = 'Milan'
# last_name = 'Matousek'
# output = 'Hello, {} {}'.format(first_name, last_name)
# print(output)
# output = 'Hello, {1} {0}'.format(first_name, last_name)
# print(output)

# convertions
# str() int() float()

# #cas a datum
# from datetime import datetime, timedelta
# # today = datetime.now()
# # print('Today is: ' + str(today))
# # one_day = timedelta(days=1)
# # yesterday = today - one_day
# # print('Yesterday was: '  + str(yesterday))
# # print('Day: ' + str(today.day)) #.month .year
# birthday = input('When is your birthday (dd/mm/yyyy)? ')
# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# print('Birthday: ' + str(birthday_date))
