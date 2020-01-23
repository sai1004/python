""" 1.Search for particular word in file, word should be taken from user input. """
word = open('demo.txt', 'r')

# chunks The para/sentence into words and stores as elements in list format
search = word.read().split(' ')

# Taking User input
userInput = input('please Enter The word you Want to search in File?')

# Using Membership Operator to check whether The user Input is in file
if userInput in search:
    print('word exists in File')
else:
    print('word does not exists in File')


""" 2. Count how many times that The Particular word is in the file.. """
word = open('demo.txt', 'r')

# chunks The para/sentence into words and stores as elements in list format
search = word.read().split(' ')

# Taking User input
userInput = input('please Enter The word you Want to Count in File?')

# Using Membership Operator to check whether The user Input is in file
if userInput in search:
    count = search.count(userInput)
    print('The Word You Entered Is: ({}) is {} times in File'.format(userInput, count))
else:
    print('word does not exists in File')
