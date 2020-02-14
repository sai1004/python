""" What is the pass statement in Python """

# There may be times in our code when we haven’t decided what to do yet,
# but we must type something for it to be syntactically correct. In such a case,
# we use the pass statement.


def func(*args):
    print('ha ha ha ', *args)


pass

print(func('hey'))


"""  Similarly, the break statement breaks out of a loop. """

for i in range(8):
    if i == 4:
        break
    print(i)


"""  Finally, the continue statement skips to the next iteration.  """

for i in range(8):
    if i == 4:
        continue
    print('contineu', i)


"""   How do you get a list of all the keys and values in a dictionary  """

mydict = {'a': 1, 'b': 2, 'c': 3, 'e': 5}

print(mydict.keys())

print(mydict.values())

for k, v in mydict.items():
    print('key -->', k + ' value -->', v)

"""   How do you insert an object at a given index in Python  """

a = [1, 2, 3]

a.insert(0, 5)  # 1st arg is for position of index, 2nd is for value

print(a)

"""   how do you reverse a list """

a.reverse()

print(a)

print(locals())


""" How will you remove a duplicate element from a list """

demo_list = [1,2,1,3,4,2]

print(set(demo_list))
