def isPrime1(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def isPrime2(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))

# isPrime1 is more readable whereas i made isPrime2 which is more compact
# use according to ur wish

for i in range(a := int(input('Enter lower limit:')), b := int(input('Enter upper limit:'))+1):
    if isPrime2(i):
        print(i, 'is prime')
