""" file reading  """

fileR = open('demo.txt', 'r')

fileR = fileR.read(10)

tel = fileR.tell()
print(tel)

# sec = fileR.tell()

# print(sec)

# fileR.close()


""" file writting  """

# filew = open('demo.txt', 'w' )

# filew.write('This line is written by python code using write mode ')

# filew.close()

""" file updating """

# fileUp = open('demo.txt', 'a')

# fileUpdate.write('\n this line is written by python code using append mode to update the file')

# fileUpdate.close()
