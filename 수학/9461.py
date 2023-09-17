import sys
P = [1,1,1,2,2,3,4,5,7,9]
for i in range(10, 100):
    P.append(P[i-3] + P[i-2])

T = int(sys.stdin.readline())
for _ in range(T):
    x = int(sys.stdin.readline())
    print(P[x-1])

