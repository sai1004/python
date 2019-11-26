Q1) What will be the output of the following statement?
>> >"a"+"bc"

output: abc

Q2) What will be the output of the following Python code?

>> > str1='hello'
>> > str2=','
>> > str3='world'
>> > str1[-1:]

output:
hello,
world
o


Q4)Write a program that accepts user's full name e.g. Albert Watson.
Print first name in the first line and last name in the second line?
# way one
user=input("Enter first name and second name: ")

users=user.split(' ')
for x in users:
    print(x)

# way two
user=input("Enter full name")
print(user.split()[0])
print(user.split()[1])

# way three
print(user)
name=input("Enter Your Full Name:")
names=name.replace(' ', '\n')
print(names)

output:
	Albert
	Watson

Q5) Request user to input any fruit name. Print that fruit name thrice?

furit=print('Enter your fav furit:')

furit *= 3
print(furit)

fruitName=input("Enter any fruit name: ")

fruit=(fruitName + " ") * 3

# fruit = (fruitName + "\n") * 3 this breaks the line
print(fruit)


output: apple apple apple
