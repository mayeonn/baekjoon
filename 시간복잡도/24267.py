import sys
cnt = 0
n = int(sys.stdin.readline())

for i in range(1, n-1):
    for j in range(i + 1, n):
        for k in range(j+1, n+1):
            cnt+=1

print(cnt)
print(3)