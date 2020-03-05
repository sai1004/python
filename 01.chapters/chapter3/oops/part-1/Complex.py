""" Complex Numbers """


class Complex:

    """ This Class Simulates Complex Numbers. """

    def __init__(self, real=0, img=0):
        if(type(real) not in (int, float)) or type(img) not in(input, float):
            raise Exception("Args Are Not Numbers!")
        # instance Var | # constructor Variable argument
        self.real = real
        self.img = img

# Creating Instance Of a Class

# try:

#     c = Complex(1, 1)
#     print("Complex Number is:", c.real, c.img)

# except Exception as e:
#     print(e)


try:

    c = Complex(2, 4)
    print(c.real, c.img)

except Exception as e:
    print(e)
