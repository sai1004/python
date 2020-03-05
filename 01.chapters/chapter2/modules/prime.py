
def isPrime(n):
    for i in range(2, int(n / 2+1)):
        if not n % i:
            return False
    return True


def primesTo(n):
    for x in range(2, n):
        if isPrime(x):
            print(x)
