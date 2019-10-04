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
 
#========================================
    
for i in range(1, 6):
    for j in range(0,i):
        print(i, end = " ")
    print("")
    
# =====================================
k = 0

for i in range(1,6):
    j = k
    for k in range(j,j+i):
        print(k, "", end=" ")
    k +=1
    print("")
    
 
# Problem 5: Allow user to input a sentence. Create a List of Words in sentence using List Comprehension.
# Create another list that would give length of corresponding word in a list.

#Important: Exclude repeating words in a list.


city = [ 'paris', 'New Delhi', 'Goa', 'MumBai', 'New York']


for i in city:
    print(i , 'char length is:', len(i))
    

#=======================================================

#Problem 6: write a program that extracts only +ive numbers from a list.
 
 numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

for x in numbers:
    if x > 0:
        print(x)
    

# Problem 7: Make a program that gives the following output. You should use a for loop in your solution.
 
#using for loop
for i in range(0,11):
    multiply = 4 * i
    print('4 multiplied by '+ str(x) +" is "+ str(multiply))

# using While loop
while i in range(0,11):
    multiply = 4 * i
    print('4 multiplied by '+ str(x) +" is "+ str(multiply))
    
    
    
    
 
# Problem 8:  Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order.
# Create a function merge that gets these lists as parameters and returns a new sorted list L that has all
# the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both 
# lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method. 
# You can however use these functions in the main function for creating inputs to the merge function. 

# Note: In Python argument lists are passed by reference to the function, they are not copied! Make sure you don’t
# modify the original lists of the caller.

L1 = [0,10,30,40,50]
L2 = [60,33,-55,-44,-22]

def merge(L1,L2):
    L = []
    sorting = L1 + L2
    while sorting:
        minimum = sorting[0]
        for x in sorting:
            if x < minimum:
                minimum = x
        L.append(minimum)
        sorting.remove(minimum)

    return L

print(merge(L1,L2))







    
# ASSIGNMENT On 30TH Sep 19:
# print th square of all numbers from 0 to 10.

for i in range(0,11):
    i **= 2
    print(i)
    
    
    
    
    
    

