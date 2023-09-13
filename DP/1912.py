import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


for i in range(n):
    temp = [arr[i]]
    
    for j in range(i, n-1):
        temp.append(temp[-1] + arr[j+1])
    arr[i] = max(temp)

print(max(arr))