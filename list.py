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
