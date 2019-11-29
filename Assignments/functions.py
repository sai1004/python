# Problem 6: write a program that extracts only +ive numbers from a list.
# Example:
#numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#Result: [34.6, 44.9, 68.3, 44.6, 12.7]


# sum_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 16, 19]

# for i in range(sum_list[0], sum_list[len(sum_list) - 1]):
#     if i not in sum_list:
#         print(i)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


for j in numbers:
    if j >= 0:
        print(j)


# admin = input("Enter the Elements: ")
# list(admin)  # converts tupple to list as array
