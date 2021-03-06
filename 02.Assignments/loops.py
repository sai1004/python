""" for loops """

import math
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


sumOfList1 = sum(list1)

avgList1 = (sumOfList1 * 20) / 100

print('The Avg Numbers Of the List is: ' + str(avgList1))


# add all even from a list , print sum of all even numbers

evenList = []

for i in list1:
    # reminder of item (i) is equals to 0 then print value of item
    if i % 2 == 0:
        evenList.append(i)
sumEven = sum(evenList)
print('The Sum Of Even Numbers in List is: ' + str(sumEven))

# """""""""""""""""" add all odd from a list , print sum of all odd numbers  """""""""""""""""""""""""""

oddList = []

for i in list1:
    # reminder of item (i) is equals to 1 then print value of item
    if i % 2 == 1:
        oddList.append(i)
sumOdd = sum(oddList)
print('The Sum Of Odd Numbers in List is: ' + str(sumOdd))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

""" ======================== print factorial Num of Input ============================ """

#  using math module
num = int(input("Please Enter Number:"))

print(math.factorial(num))

# without using math module
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)

""" ===================================== Structures =================================== """

for i in range(1, 6):
    print('* ' * i)

# ========================================

for i in range(1, 6):
    for j in range(0, i):
        print(i, end=" ")
    print("")


# =====================================
k = 0

for i in range(1, 6):
    j = k
    for k in range(j, j+i):
        print(k, "", end=" ")
    k += 1
    print("")


# Problem 5: Allow user to input a sentence. Create a List of Words in sentence using List Comprehension.
# Create another list that would give length of corresponding word in a list.

# Important: Exclude repeating words in a list.


city = ['paris', 'New Delhi', 'Goa', 'MumBai', 'New York']


for i in city:
    print(i, 'char length is:', len(i))


# =======================================================

# Problem 6: write a program that extracts only +ive numbers from a list.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

for x in numbers:
    if x > 0:
        print(x)


# Problem 7: Make a program that gives the following output. You should use a for loop in your solution.

# using for loop
for i in range(0, 11):
    multiply = 4 * i
    print('4 multiplied by ' + str(i) + " is " + str(multiply))

# using While loop
while i in range(0, 11):
    multiply = 4 * i
    print('4 multiplied by ' + str(i) + " is " + str(multiply))
    i += 1


# ASSIGNMENT On 30TH Sep 19:
# print th square of all numbers from 0 to 10.

for i in range(0, 11):
    i **= 2
    print(i)
