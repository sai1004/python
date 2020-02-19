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


# def decToBin(ip):

#     binary = ''

#     divIp = ip.split()
#     print(divIp)


# print(decToBin('192.168.31.1'))


ip = '192.168.31.1'

divIp = ip.split('.')

for i in divIp:
    print(bin(int(i)).replace("0b", ''), end='.')

    
    
    
    
    


import random # biblíoteca para gerar sequências aleatórias.  

import string # biblíoteca para tratamento de caractéres do tipo string. 

i = input("enter the password to be encrypted --> ".upper())

password = '' # Variável que armazena a nova senha 

# Percorre uma range com o valor de caractéres do texto.

for a in range(len(i)): 

    # Pega o caractére digítado e gera uma sequência aleatória com letras maiúscula,minúsculas e numeros.

    new = random.choice(i + string.hexdigits)    

    password += new # adiciona a nova senha na variavel vazia. 

print('---'*len(i))

print('New password:',password)

print('---'*len(i))    




Hacking = True

while Hacking == True:

  print('0110101010111100101010111110100100100101010001')

  print('0101010101000000011010101010010101011110101011')

  print('1010101010111111100101010101101010100001010100')

  print('1001010101000011010101000001011011011010101110')

  print('0000000011110101001010110101111110100101101001')

  print('1111111111111111111100101010100000000111010010')

  print('0000000001010010101110010100101010000101011101')

  print('0111101001010101010000010101011111010101000000')
