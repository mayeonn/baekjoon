N = int(input())
cnt = 0
while N%3%2!=0:
    N -= 1
    cnt+=1

while N!=1:
    if N%3==0:
        N /= 3
    elif N%2==0:
        N /= 2
    cnt += 1
print(cnt)