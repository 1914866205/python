def isPrime(num):
    for i in range(num):
        try:
            if(i!=1 and num%i==0 and i!=num):
                return False
        except:
            continue
    return True
print(isPrime(5))
print(isPrime(9))
