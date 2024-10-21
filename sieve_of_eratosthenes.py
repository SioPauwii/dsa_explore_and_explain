def SieveOfEratosthenes(maxNum):
    num = [True] * (maxNum + 1)
    primes = []
    p = 2
    while (p * p <= maxNum):
        if num[p]:
            for i in range(p * p, maxNum + 1, p):
                num[i] = False
        p += 1

    for p in range(2, maxNum + 1):
        if num[p]:
            primes.append(p)

    print(primes)        

SieveOfEratosthenes(100)
