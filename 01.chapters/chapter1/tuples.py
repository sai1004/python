""""""""""""""""""""""""" tuples """""""""""""""""""""""""
# tuples are imuteable in python that mean item in obj cannot be changed, Python Tuple is used to store the sequence of immutable python objects.

tuple1 = ('hello', 'world')

print(tuple1[0])
print(hex(id(tuple1)))  # prints in memory
print(type(tuple1))


t1 = (101, "Ayush", 22)

t2 = ("Apple", "Banna", "Orange")

print(t1)
print(t2)

t3 = (t1, t2)

print(t3)

# converting tuple to set
print(set(t1))

numTupple = (10, 20, 30, 40, 50, 60, 70, 80, 90)

print(numTupple)

print(numTupple[4])

print(numTupple[2:6])

# reversing a tuple
print(numTupple[::-1])

print(numTupple.index(30))

print(numTupple.count(20))

# looping a tuple
for i in numTupple:
    print(i)
