def isPrimeNum(x):
    for i in range(2,x):
        if x%i==0: return False
    return True

M = int(input())
N = int(input())
primeNumList = []

for x in range(M,N+1):
    if isPrimeNum(x):
        if x==1:
            continue
        primeNumList.append(x)

if len(primeNumList) > 0 :
    print(sum(primeNumList))
    print(primeNumList[0])
else:
    print(-1)