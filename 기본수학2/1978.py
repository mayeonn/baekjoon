def isPrimeNum(x):
    for i in range(2,x):
        if x%i==0: return False
    return True

N = int(input())
numList = list(map(int, input().split()))
cnt = 0

for x in numList:
    if isPrimeNum(x):
        if x==1:
            continue
        cnt+=1

print(cnt)