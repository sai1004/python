bikes = ['bmw', 'suzuki', 'duke']

print(bikes)

# to get first elememt in array

firstBike = bikes[0]
print(firstBike)

# to get last elememt in array

lastBike = bikes[-1]
print(lastBike)

# looping through list

for bike in bikes:
    print(bike)

""""""""""""""""""""""""" CRUD Ops in List """""""""""""""""""""""""

# adding items to a list

names = []
names.append('sai')
names.append('sammy')
names.append('chris')
print(names)

# updating the list items

names[1] = 'simon'


# removing single items

names.remove('chris')

# delets whole items in list
del(names)


# making numerical lists

squares = []

for x in range(1, 11):
    squares.append(x**2)
print(squares)

# '''''''''''''''''''''''''''' slicing the list ''''''''''''''''''''''''''''

finishers = ['sam', 'bob', 'amanda', 'linda']

firstTwo = finishers[:2]

print(firstTwo)


# in python strings and numbers are imutable  that the value of the obj or var cannot be changed in mem location

a = 2  # allocating the memory
print(hex(id(a)))
a = 30
print(hex(id(a)))  # to print the loc of mem allocation


# in python lists are mutable

price = [10, 20, 30, 40, 50]

cart = ['fruits', 'electronics', 'items']

print(price[-1])
print(price[3])
print(price[0:2])
print(price[::3])  # it takes step value

combined = price + cart

price.append(33)
print(price)
print(price.count(60))

# changing the value of list
price[0] = 60
print(price)

list1 = [22, 5, True, 78, [20, 99, 'a']]
print(list1[-1][1])

len(list1)

# reversing the string:

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lst[::-1])

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''

list1 = ['2', '5', '1', '3', '1', '5', '1', '5']

# returns the count of value, the value how many times is repeated! o/p: 3
print(list1.count('1'))

print(list1.index('5'))  # returns the index value of the '5' in list

list1.append('3')  # adding new value to the list

list1.remove('5')  # removing the value

# del(list1[:])  # deletes the whole values in list

# del(list1)
print(list1)

# list1.clear()  # removes the all the items from list

print(list1)

for x in list1:
    print(x)

print(list1)


""""""""""""""""""""""""" enumerate """""""""""""""""""""""""

my_list = ['apple', 'banana', 'grapes', 'pear']
for count, value in enumerate(my_list, 1):
    print(count, '-->', value)


lst = [
    {
        "name": "sam",
        "email": "sammy@gmail.com"
    }, {

        "name": "kiarn",
        "email": "kiran@gmail.com"
    }
]

for i in lst:
    print(i)
