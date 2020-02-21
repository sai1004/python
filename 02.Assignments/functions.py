
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


"""   Google Search """

# Install following two packages before executing the code below

# pip install beautifulsoup4

# pip install google

try:

    from googlesearch import search

except ImportError:

    print("No module named 'google' found")

# to search

query = "python for engineers Blog"

for j in search(query, tld="co.in", num=10, stop=1, pause=2):

    print(j)


# Problem 8:  Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order.
# Create a function merge that gets these lists as parameters and returns a new sorted list L that has all
# the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both
# lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method.
# You can however use these functions in the main function for creating inputs to the merge function.

# Note: In Python argument lists are passed by reference to the function, they are not copied! Make sure you don’t
# modify the original lists of the caller.

L1 = [0, 10, 30, 40, 50]

L2 = [60, 33, -55, -44, -22]


def merge(L1, L2):
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


print(merge(L1, L2))


""" ---------------------------  Linear Search --------------------------- """

def search(list,n):

    for i in list:
        if i== n:
            print(n," is found at index ",
            list.index(i)+1)
            break
    else:
        print(n, " is not found, try Again")

list= [19,5,22,18,2,6,0,100,9]


n= int (input("Enter a number to search: "))

search(list,n)
