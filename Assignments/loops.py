""" for loops """

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


sumOfList1 = sum(list1)

avgList1 = (sumOfList1 * 20) / 100

print('The Avg Numbers Of the List is: '+ str(avgList1))


# add all even from a list , print sum of all even numbers

evenList = []

for i in list1:
    if i % 2 == 0:    # reminder of item (i) is equals to 0 then print value of item
        evenList.append(i)
sumEven = sum(evenList)
print('The Sum Of Even Numbers in List is: '+ str(sumEven))

# """""""""""""""""" add all odd from a list , print sum of all odd numbers  """""""""""""""""""""""""""

oddList = []

for i in list1:
    if i % 2 == 1:   # reminder of item (i) is equals to 1 then print value of item
        oddList.append(i)
sumOdd = sum(oddList)
print('The Sum Of Odd Numbers in List is: '+ str(sumOdd))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

""" print factorial Num of Input """

#  using math module 
import math
num = input("Please Enter Number:")

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
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

"""  Structures  """

for i in range(1, 6):
    print('* ' * i)
    
    
for i in range(1, 6):
    for j in range(0,i):
        print(i, end = " ")
    print("")
    
    

