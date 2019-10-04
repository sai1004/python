# Problem 8:  Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order.
# Create a function merge that gets these lists as parameters and returns a new sorted list L that has all
# the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both 
# lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method. 
# You can however use these functions in the main function for creating inputs to the merge function. 

# Note: In Python argument lists are passed by reference to the function, they are not copied! Make sure you don’t
# modify the original lists of the caller.

L1 = [0,10,30,40,50]

L2 = [60,33,-55,-44,-22]

def merge(L1,L2):
    L = []
    sorting = L1 + L2
    while sorting:
        minimum = sorting[0]
        for x in sorting:
            if x < minimum:
                minimum = x
        L.append(minimum)
        sorting.remove(minimum)

    return L

print(merge(L1,L2))

