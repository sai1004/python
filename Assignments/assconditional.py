""" without logical operator """

n1 = int(input('Please Eneter a Number: '))
n2 = int(input('Please Eneter a Number: '))
n3 = int(input('Please Eneter a Number: '))

arr = n1, n2, n3
parse = list(arr)
print('The MAX Number Of n1,n2,n3: ', str(max(parse)))
print('The MIN Number Of n1,n2,n3: ', str(min(parse)))

""" with logical operator """

if n1 > n2 and n1 > n3:
    print("The Largest Number of n1,n2,n3  with logical operator is:", n1)
elif n2 >= n1 and n2 >= n3:
    print("The Largest Number of n1,n2,n3  with logical operator is:", n2)
else:
    print("The Largest Number of n1,n2,n3  with logical operator is:", n3)


# 3) Take 10 inputs from the user as Number and do sum of all ten numbers and
#    get avg of sum, also write if statement

userInput = input('Please Enter the Numbers :')

parse = list(userInput)

sum = sum(parse)
print(" Your Total out of 600 is: " + str(sum))
avg = sum * 100 / 600

print(' Your Avg Score out of 100%: ' + str(avg)+'%')

if avg >= 90:
    print(' The Perfomance is very good keep it up')

elif avg >= 60:
    print(' The Perfomance is good')

else:
    print(' The Perfomance is bad, You Need To Try Hard ')
