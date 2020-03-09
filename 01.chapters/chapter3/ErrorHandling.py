try:
    lst = [1, 2, 3, 4, 5, 6]
    for i in lst:
        print(jgjh)

except:

    print("somthing Went Wrong")

finally:
    """ It will print After The Error handling, it doesn't care about result error or correct """
    print(" I Printed after try And Exception ")


try:
    print("hello world!")

except Exception as e:
    print(e)

try:
    import requests

except ImportError:
    print(" requests module not found!")