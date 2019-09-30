""" without logical operator """

n1 = int(input('Please Eneter a Number: '))
n2 = int(input('Please Eneter a Number: '))
n3 = int(input('Please Eneter a Number: '))

arr = n1, n2, n3
parse = list(arr)
print(max(parse))
print(min(parse))

if (n1 >= n2 ) and ( n1 >= n3):
    max = n1
elif (n2 >= n1 ) and (n2 >= n3):
    max = n2
else:
    max = n3
    print("The Largest Number of n1,n2,n3 is:", max)
# 3) Take 10 inputs from the user as Number

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
