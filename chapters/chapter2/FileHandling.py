""" =============================== File Open Write Mode (Over Writes)========================== """

fw = open('demo.txt', 'w')

print(fw.write('hey hi'))

fw.close()

""" =================================== File Open Read Mode ======================================== """
fr = open('demo.txt', 'r')

print(fr.read())
print(fr.tell())  # tells the current pointer position of element in file
print(fr.seek(0))
print(fr.read())

fr = open('demo.txt', 'r')
print(fr.read())

fr.close()

""" =============================== File Open Append (Update) Mode =============================== """

fa = open('demo.txt', 'a+')
fa.write('this line is appended')
print(fa.read())  # returns the empty string
print(fa.tell())
print(fa.seek(0))
print(fa.read())


# Can also use Slicing method

print(fa.read()[0:5])

fa.close()
