import sys
N, X = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
for i in range(N-1):
    if(a[i]<X): print(a[i], end=' ')
if(a[N-1]<X): print(a[N-1])