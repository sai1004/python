# Problem 6: write a program that extracts only +ive numbers from a list.
# Example:
#numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#Result: [34.6, 44.9, 68.3, 44.6, 12.7]


# sum_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 16, 19]

# for i in range(sum_list[0], sum_list[len(sum_list) - 1]):
#     if i not in sum_list:
#         print(i)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


for j in numbers:
    if j >= 0:
        print(j)


# admin = input("Enter the Elements: ")
# list(admin)  # converts tupple to list as array

person = {
    'name': 'sam',
    'email': 'sam@example.com',
    'mobile': 123456789,
    'gender': 'male'
}

print(person)

for k, v in person.items():

    print(k, ' --> ', v)


# getMissingNo takes list as argument 
def getMissingNo(A): 
    n = len(A) 
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A) 
    return total - sum_of_A 

# Driver program to test above function 
A = [1, 2, 4, 5, 6] 
miss = getMissingNo(A) 
print(miss) 


plainText = 'Hello I\'m the king'


def encrypt(string):
    cipher = []
    reSpace = string.replace(' ', '')[::-1]
    for char in reSpace:
        codes = ord(char)
        cipher.append(codes + 1)
    return cipher


print(encrypt(plainText))


def decrypt():
    deCipher = ''

    decCodes = encrypt(plainText)
    for code in decCodes:
        chars = chr(code - 1)
        deCipher += chars  # equals to deCipher + deCipher = chars
    return deCipher[::-1]


print(decrypt())
