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


"""" ==========================  args and **kwargs ========================= """

# 1.1. Usage of *args


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


# 1.2. Usage of **kwargs

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="yasoob")


def add_to(num, target=[]):

    target.append(num)
    print(target)
    return target


num = input("enter nums")
add_to(num)


def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target


def callme(*args, **kargs):
    for key in args:
        print(key)
    for value in kargs:
        print(value)


callme('1st parameter', '2nd parameter')


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
