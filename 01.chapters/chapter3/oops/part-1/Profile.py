"""  Counting the number of objects of a class  """


class Profile:

    count = 0

    def __init__(self):

        Profile.count = Profile.count + 1


p1 = Profile()

p2 = Profile()

p3 = Profile()

print("The Number Of Profiles: ", Profile.count)
