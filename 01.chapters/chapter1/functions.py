""""""""""""""""""""""""" args and **kwargs  """""""""""""""""""""""""

# 1.1. Usage of *args


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


# 1.2. Usage of **kwargs

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")


def add_to(num, target=[]):
    target.append(num)
    print(target)
    return target


# num = input("enter nums")
# add_to(num)


# def add_to(element, target=None):
#     if target is None:
#         target = []
#     target.append(element)
#     return target


# def callme(*args, **kargs):
#     for key in args:
#         print(key)
#     for value in kargs:
#         print(value)


# callme('1st parameter', '2nd parameter')

""""""""""""""""""""""""" Convert Decimal to binary """""""""""""""""""""""""

ip = '192.168.31.1'

divIp = ip.split('.')

for i in divIp:
    print(bin(int(i)).replace("0b", ''), end='.')
    

"""  password gen    """
    
import random    

import string  

i = input("enter the password to be encrypted --> ".upper())

password = '' 

for a in range(len(i)):  

    new = random.choice(i + string.hexdigits)    

    password += new  

print('---'*len(i))

print('New password:',password)

print('---'*len(i))    