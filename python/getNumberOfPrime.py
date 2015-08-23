import math

def  getNumberOfPrimes( n):
    if n <= 2:
        return 0
    counter = 0
    for i in range(3,n,2):
        if isPrime(i):
            counter += 1
    return counter + 1
                
def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
