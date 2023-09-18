import sys
num = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(5):
    answer += num[i]**2

print(answer%10)