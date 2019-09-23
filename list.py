bikes = [ 'bmw', 'suzuki', 'duke' ]

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

# adding items to a list

names = []
names.append('sai')
names.append('sammy')
names.append('chris')
print(names)


# making numerical lists

squares = []

for x in range(1,11):
    squares.append(x**2)
print(squares)

# <======================= slicing th list =======================>

finishers = ['sam','bob','amanda','linda']

firstTwo = finishers[:2]

print(firstTwo)


# in python strings and numbers are imutable  that the value of the obj or var cannot be changed in mem location

a = 2 # allocating the memory
print(hex(id(a)))
a = 30
print(hex(id(a))) #to print the loc of mem allocation


# in python lists are mutable 

price = [ 10, 20, 30, 40, 50]

cart = ['fruits','electronics','items']

print(price[-1])
print(price[3])
print(price[0:2])
print(price[::3]) #it takes step value

combined = price + cart

price.append(33)
print(price)
print(price.count(60)) # returns true or false if value exists returns 1(true)

#changing the value of list
price[0] = 60
print(price)

list1 = [ 22, 5, True , 78 , [20, 99, 'a']]
print(list1[-1][1])

len(list1)
print(max(list1))
print(min(list1))

