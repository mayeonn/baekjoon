limit = 123456
sieve = [True]*(2*limit + 1)
sieve[0] = False
sieve[1] = False

for x in range(2, int((2*limit + 1)**0.5)):
    if sieve[x]:
        for i in range(x+x, 2*limit + 1, x):
            sieve[i] = False

N = int(input())

while N!=0:
    cnt = 0

    for i in range(N+1, 2*N + 1):
        if sieve[i]:
            cnt += 1

    print(cnt)
    N = int(input())