# There are two types of division operations in python.

# 1. Ordinary division, with / operator
# 2. Floor division, with // operator


""""""""""""""""""""""""" Arithmetic Oprator """""""""""""""""""""""""
#  Operators: + ,- ,*, / ,//, **, %

a = 10
b = 20
c = 10

print(a + b)
print(a - b)
print(b - c)
print(c * b * a)
print(a*b/2*25//3)


print(10 / 5)   # rturns float value
print(10 // 5)  # retruns int value

print(5 / 2)
print(5 // 2)

print(7 // 3)
print(5 // 2)

5

print(5 % 2)  # returns remainder of 5/2

print(5 ** 3)  # 5 * 5 * 5 = 125

""""""""""""""""""""""""" Comparision Operator """""""""""""""""""""""""


a = 10
b = 20
c = 10

print(a == c)
print(a == b)

print(a != b)
print(a != c)

print(10 == 10)
print(10 > 11)

print(10 >= 10)
print(20 <= 20)


""""""""""""""""""""""""" assignment operators """""""""""""""""""""""""

# =, +=, -=, *=, /=, %=, //=, **=
#
# (a = a + 10)  is equal to (a += 10)
a = 20
a += 100
print(a)

a *= 2
print(a)

""""""""""""""""""""""""" bitwise Operators """""""""""""""""""""""""


# & (binary AND)
# | (or)
# << (binary left shift )
# >> (binary right shift)
# ^ binary XOR
# ~ binary ones complement

# <==== Number System ====>

# hexadecimal -> 0-9,a,b,c,d,e,f;
# decimal -> 0-9      (2309)base 10;
# octal -> 0-7
# binary -> 0 1

# a = 10 # 0001 0000
# b = 20 # 0010 0000

""""""""""""""""""""""""" Logic Operators """""""""""""""""""""""""

# and, or, not
# F             #F       = FALSE
# print((10 > 20) and ( 30 > 40))

# print((10 > 20) or ( 30 > 40))

# print((10 > 9 ) and ( 50 > 40))

x = 10
y = 15

z = (x < y) and (y > x)
print(z)

w = y > x / 2 and x < y
print(w)

# not operator

print(not (x > 20 > y))


""""""""""""""""""""""""" membership oprators """""""""""""""""""""""""


# in

# not in

list1 = [20, 30, 40, 50]

print(60 not in list1)
print(60 in list1)

""""""""""""""""""""""""" identity operator """""""""""""""""""""""""

# is
# is not

a = 10
b = 10


print(id(a))  # | memory location stores as same value so the output will true
print(id(b))  # |

print(a is b)

print(a is not b)


""""""""""""""""""""""""" Chained comparision operator """""""""""""""""""""""""

a, b, c = 10, 20, 30

print(a < b < c)
print(a == b < c)
