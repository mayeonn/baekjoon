import sys

n = int(sys.stdin.readline())
triangle = [[0 for _ in range(i)] for i in range(n)]

for i in range(n):
    triangle[i] = list(map(int, sys.stdin.readline().split()))
    

for i in range(1, n):
    for j in range(i+1):
        if j==0:
            triangle[i][j] += triangle[i-1][j]
        elif j==i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i][j]+triangle[i-1][j], triangle[i][j]+triangle[i-1][j-1])

print(max(triangle[n-1]))