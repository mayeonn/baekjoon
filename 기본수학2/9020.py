limit = 10000
sieve = [True]*(2*limit + 1)
sieve[0] = False
sieve[1] = False

for x in range(2, int((2*limit + 1)**0.5)):
    if sieve[x]:
        for i in range(x+x, 2*limit + 1, x):
            sieve[i] = False


T = int(input())

for _ in range(T):
    n = int(input())
    for x in range(n//2, n):
        if(sieve[x] and sieve[n-x]):
            print("%d %d" %(n-x, x))
            break