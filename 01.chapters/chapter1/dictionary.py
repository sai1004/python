""""""""""""""""""""""""" Dictionary: A Python dict Obj is an unordered collection of data in a key-value pair """""""""""""""""""""""""


# dict are muteable in python that you can chage value of obj in dict
# cannot access the index value it throws key val err

# dict() function inbulit


fruits = {'apple': 50, 'grape': 30, 'orange': 40, 'kiwi': 25, 1: 56}
fruits['apple'] = 100  # can change the val
print(fruits[1])

# fruits.keys()
# fruits[0] #throws key err: 0 dosen't exists
# print(fruits.keys())
# print(fruits.values())

# for x in fruits:

# print(x)


# profile1 = {
#     "name":"kiarn",
#     "email":"kiran@gmail.com"
# }

# profile2 = {
#         "name":"sam",
#     "email":"sammy@gmail.com"
# }


""""""""""""""""""""""""" Dicitionaries  """""""""""""""""""""""""

alien = {'color': 'green', 'points': 5}

# assigining a value

print("The alien's Color is " + alien['color'])

# adding new key-value pair

alien['from'] = 'UFO'

print(alien)


""""""""""""""""""""""""" looping through all key-value pairs """""""""""""""""""""""""

fav_nums = {'eric': 17, 'dona': 4}

for name, number in fav_nums.items():
    print(name + ' loves ' + str(number))

# looping through all the values

fav_nums = {'eric': 17, 'dona': 4}

for number in fav_nums.values():
    print(str(number) + ' is a fav')


dict1 = {1: 2, 3: 4}
for k, v in dict1.items():
    print(v)
