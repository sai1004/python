import os

""""""""""""""""""""""""" Printing the Current Working Directory """""""""""""""""""""""""

# In order to get the current working directory, you need to use os.getcwd()

print("The Current Wroking directory: ", os.getcwd())

""""""""""""""""""""""""" Creating Directories """""""""""""""""""""""""
# To make a folder/directory in any operating system, all you need to do is:

# os.mkdir("NewFolder")  # makes an empty directory

# running mkdir again with the same name raises FileExistsError, run this instead:

try:
    if not os.path.isdir("NewFloder"):
        os.mkdir("NewFolder")
        print('Folder Created SuccessFully ')
except:
    print('Folder Already Exists Cannot Be Created Again With Same Name')
