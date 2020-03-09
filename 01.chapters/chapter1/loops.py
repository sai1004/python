""""""""""""""""""""""""" for loops """""""""""""""""""""""""

for i in range(0, 11):  # range(start,stop,step) stop = n - 1
    print(i)

for i in range(1, 11):
    print(i ** 2)


colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)


""""""""""""""""""""""""" While Loops """""""""""""""""""""""""

#  prints 0 - 10 numbers in one line without breaking line:

n = 0
while n < 10:
    print(n, end=" ")
    n = n + 1

#  prints 0 - 10 numbers in one line with breaking line:

n = 0
while n <= 10:
    n += 1
    print(n)


# print first ten even numbers

#   using two var:
n = 2
i = 1
while i <= 10:
    print(n)
    n += 2
    i += 2

#   using only one var:

n = 0

while n <= 20:
    n += 2
    print(n)


# KeyWords: break, continue, pass

# print 0-10 break where n == 5, stops at 5

n = 0

while n <= 10:
    n += 1
    if n == 5:
        break
    print(n)

# print 0-10 continue where n == 5, continue at 6


n = 1
while n <= 10:
    if n == 5:
        n += 1
        continue
    print(n, end=" ")
    n += 1


# print 0-10 pass where n == 5, pass

n = 1

while n <= 10:
    if n == 5:
        print(n ** 2, end=" ")
        pass
    else:

        print(n, end=" ")
    n += 1

# ==================================

counter = 1

while counter <= 5:
    n = 1
    while n <= counter:
        print("Hello", end=" ")
        n += 1
    print()
    counter = counter + 1


""" For Fun """

Hacking = True

while Hacking == True:

    print('0110101010111100101010111110100100100101010001', end="")


""""""""""""""""""""""""" List Comprehense: """""""""""""""""""""""""


city = "New Delhi"

listCityChar = []

for letter in city:
    listCityChar.append(letter)

print(listCityChar)


city = "New Delhi"

lCity = [ch for ch in city]

print(lCity)

lNum = [n for n in range(2, 21)]
print(lNum)

lEven = [n for n in range(2, 21, 2)]
print(lEven)

lEven = [x for x in [n for n in range(2, 21, 2)][0:5]]
print(lEven)

nNum = [n for n in range(2, 21) if n % 2 == 0]
print(nNum)


# Assume backet is under the tap , filling backet with water , count the backets while filling,
# and off the tap when backet is filled 3 backets .

count = 0
while True:
    backet = int(input("Enter The Current Backet Filled Number:"))
    count = backet
    print(count)
    if count >= 3:
        print('Tap is offed Limit exhausted')
        break
