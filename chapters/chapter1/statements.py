""""""""""""""""""""""""" if statements """""""""""""""""""""""""

# conditional tests
x = 42

x == 42    # equals

x != 42   # not equal

x > 42   # greater than

x >= 42  # or equal to

x < 42  # less than

x <= 42  # or equal to

names = ['james', 'bond', 'alex']

if 'alex' in names:
    print(names)
    print('hello {} you are warned dont not repeate again!'.format('alex'))

if 'sai' not in names:
    print(names)
    print('Sorry please wait for {} to Come in'.format('sai'))

game_active = True

can_edit = False


age = 5
if age < 4:
    ticketPrice = 0
    print(" Ticket For Age Less Than 4:", ticketPrice)
elif age < 18:
    ticketPrice = 10
    print(" Ticket For Age Less Than 18: {}".format(ticketPrice))

else:
    ticketPrice = 15
    print(" Ticket For Age Less Than 18: {}".format(ticketPrice))


""""""""""""""""""""""""" user Input  """""""""""""""""""""""""

name = input('Whats Your Name?')

print('Hello,' + name)  # names in str format

pi = input('What is the value of PI ?')
pi = float(pi)
if pi != 3.14159265:
    print('wrong')


a = 10
b = 1

if a != b:
    print('True')
else:
    print('False')
