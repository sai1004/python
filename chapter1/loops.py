"""  for loops  """




""" While Loops """

#  prints 0 - 10 numbers in one line without breaking line:

n = 0
while n < 10:
    print(n, end=" ")
    n = n + 1
    
#  prints 0 - 10 numbers in one line with breaking line:

n = 0
while n <= 10:
    n += 1
    print(n)
      
      

# print first ten even numbers

#   using two var: 
n = 2
i = 1
while i <= 10:
    print(n)
    n += 2
    i += 2

#   using only one var:

n = 0 

while n <= 20:
    n += 2
    print(n)
    
    
# KeyWords: break, continue, pass

# print 0-10 break where n == 5, stops at 5

n = 0

while n <= 10:
    n +=1
    if n == 5:
        break
    print(n)
    
# print 0-10 continue where n == 5, continue at 6


n = 1
while n <= 10:
    if n == 5:
        n +=1
        continue
    print(n, end=" ")
    n +=1


# print 0-10 pass where n == 5, pass

n = 1

while n <= 10:
    if n == 5:
        print( n ** 2, end=" ")
        pass
    else:

        print(n, end=" ")
    n +=1

# ==================================

counter = 1

while counter <= 5:
    n = 1
    while n <= counter:
        print("Hello", end=" " )
        n += 1
    print()
    counter = counter + 1

