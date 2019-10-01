""" for loops """

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# add all even from a list , print sum of all even numbers

evenList = []

for i in list1:
    if i % 2 == 0:
        evenList.append(i)
sumEven = sum(evenList)
print(sumEven)

# """""""""""""""""" add all odd from a list , print sum of all odd numbers  """""""""""""""""""""""""""

oddList = []

for i in list1:
    if i % 2 == 1:
        oddList.append(i)
sumOdd = sum(oddList)
print(sumOdd)
