""""""""""""""""""""""""" file reading """""""""""""""""""""""""

file_read = open('demo.txt', 'r')

file_read = file_read.read(10)

tel = file_read.tell()
print(tel)

# sec = file_read.tell()

# print(sec)

# file_read.close()


""""""""""""""""""""""""" file writting """""""""""""""""""""""""

# filew = open('demo.txt', 'w' )

# filew.write('This line is written by python code using write mode ')

# filew.close()

""""""""""""""""""""""""" file updating """""""""""""""""""""""""

# fileUp = open('demo.txt', 'a')

# fileUpdate.write('\n this line is written by python code using append mode to update the file')

# fileUpdate.close()
