""" The elements of the python set must be immutable. """

iamset = {1, 2, 3, 4}


Days = {"Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"}
print(Days)
print(type(Days))



print("looping through the set elements ... ")
for i in Days:
    print(i)