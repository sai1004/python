""" dealing with strings """

city = 'New York'  #length of the string is 8 the length key word start reads from 1 to end not from 0, so consider n-1

print(city)

#indexing String

print(city[0]) #from left to right forward bais

print(city[-1])

print(city[3]) #in String empty space is also considered as index value it returns empty value

# <================ slicing the string ==================>
# in slice method in the box(arry) the value 0 [start , end, step]
print(city[0:8:2])

# print(city[0:3])

print(city[-4:-7]) # it wont return any value cause it only reads from left to ringht

print(city[-4:-7:-1]) #this will return till the one step point

print(len(city))

sentence = 'alexa likes ,siri but siri wont'

print(sentence.split(','))

email = 'example@domain.com'

emailSplited = email.split('@')[0]

print(emailSplited)

""" end keyword """

test = "hello "

print(test, end =" world ")
