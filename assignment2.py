ASSIGNMENT 1
Get the user input about the current position of the employee and his performance grade.
Performance cutoff is 90% if the performance is moRe than 90% promote him. 
If not degrade him. 

#input 10,20,30,92,40,5,6,70

admin = input("Enter the Elements: ")
list(admin) # converts tupple to list as array

print(max(admin))
avg = max(admin)

if avg >= 90:
    print("You are Promoted to Super Admin!")
else:
    print("Better luck Next time, You're not admin any more.")
