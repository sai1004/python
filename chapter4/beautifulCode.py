""" old way """

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i ** 2)

""" New way """

for i in range(10):
    print(i ** 2, end=" ")


# ===============================================
colors = ['red', 'green', 'blue', 'yellow']


""" old way """

for i in range(len(colors)):
    print(colors[i])

""" New way """
for color in colors:

    print(color)

# =============================================

""" looping backwards """

""" old way """

for i in range(len(colors)-1, -1, -1):
    print(colors[i])

""" New way """

for color in reversed(colors):
    print(color)

# =========================================================
""" Looping Over a Collection and Indicies. """


for i in range(len(colors)):
    print(i, '-->', colors[i])
