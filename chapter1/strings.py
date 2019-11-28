# https://pysnakeblog.blogspot.com/2019/09/top-40-python-string-processing-in.html?m=1
# """ dealing with strings """

# city = 'New York'  # length of the string is 8 the length key word start reads from 1 to end not from 0, so consider n-1

# print(city)

# # indexing String

# print(city[0])  # from left to right forward bais

# print(city[-1])

# # in String empty space is also considered as index value it returns empty value
# print(city[3])

# # <================ slicing the string ==================>
# # in slice method in the box(arry) the value 0 [start , end, step]
# print(city[0:8:2])

# # print(city[0:3])

# # it wont return any value cause it only reads from left to ringht
# print(city[-4:-7])

# print(city[-4:-7:-1])  # this will return till the one step point

# print(len(city))

# sentence = 'alexa likes ,siri but siri wont'

# # reversing string
# print(sentence[::-1])

# print(sentence.split(','))

# email = 'example@domain.com'

# emailSplited = email.split('@')[0]

# print(emailSplited)

# """ end keyword """

# test = "hello "

# print(test, end=" world \n")


# ============================================================part 2===============================================


a = 'python'
b = 'blog'
c = 'tutorial'
d = 'is'
e = 'awesome'

print(a)
print(b)
print(c)
print(d)
print(e)

print(a, b, c, d, e)

# combining all the var

print(a+b+c+d+e)

# breaking the line
print(a+'\n'+b+'\n'+c+'\n'+d+'\n'+e)

# ===========================  string mainpulation ===============================

# _5 string indexing and manipulating (subscript notation)
# string index starts from 0

print(a[0])

print(b[1])

print(c[2])

# print(d[3]) error throws out of index range

# _6 manipulating string

print(a[0]+b[1]+e[0]+a[5]+e[2]+c[0])


# _7 slicing string

print(a[0:3])  # prints 0 to n-1

print(b[1:3])

print(c[0:4:2])  # can take three arg (start,stop,step)

print(e[::2])  # skips the step number


# _8 negative index slicing string

print(a[-1:])  # -ve index value takes the last of value the string


# this is not possible in slicing the value should start from lower limit to upper limit in string left to right
print(a[-1:-4])

print(a[-7:-4])  # this is okay

print(b[-6:-3])

print(c[-1::-1])

# _9 string operator %

print(' %(placeholder)s' % {"placeholder": "XXXX"})


print(' %(placeholder)s' % {"placeholder": "hello i\'m placeholder"})


# _10 string operator % using integer

print(' %(integer)d' % {"integer": 1})
print(' %(integer)01d' % {"integer": 1})
print(' %(integer)02d' % {"integer": 1})
print(' %(integer)03d' % {"integer": 1})


print('%s %s %d %d %f %f' % ('Hercules', 'Zeus', 100, 20, 3.2, 1))

# manipulate string to integer

d = '365'

print(10 * int(d))

print((a + ' ') * 5)  # concatenating str with white space

print('7' + '4')

print(float('7') + float('4'))

# common methods for string class

# counting letter 'o'

text = "It is so simple to be happy but it is so difficult to be simple"


print(text.count('o'))

print(text.upper())
print(text.lower())

# join text with space ' '

print(' '.join(text))

# split text where ever space ' ' is present

print(text.split(' '))

# text = 'what a wonderful world'

# for letter in text:
#     print(letter, end='')

up_text = text.upper()

print(up_text.isupper())

print(up_text.islower())

# contains both letters and numbers

print(text.isalnum())

new_text = "H2SO4"
print(new_text.isalnum())

# character count
print(len(text))

# _26 converts character to decimal

print(ord('A'))

print(ord('B'))

print(ord('a'))

# converts decimal back to character

print(chr(65))

print(chr(118))

# the backslash is needed to escape the apostrophe.

print('What\'s up?')

# triple quotes can escape single, double, and a lot more.

print("""What's up? Does the "" need an escape?""")

# The format string syntax was introduced in python3

var_1 = 'test'

var_2, var_3 = 'move it move it', 'MOVE IT!'

print('This is a {}'.format(var_1))
print('This is a {}'.format(var_2))

#  accessing arguments by name

print('Mount Whitney is Located at {latitude}°N , and {longitude}°W'.format(
    latitude='35.5785', longitude='118.2923'))


# accessing arguments' items:

point = (5, 10)
print('The point values are {0[0]} and {0[1]}'.format(point))
