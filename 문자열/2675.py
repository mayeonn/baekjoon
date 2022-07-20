import sys
N = int(input())
for i in range(N):
    P = ''
    S = list(sys.stdin.readline().strip())
    R = int(S[0])
    S = S[2:]
    for j in S:
        P = P + j*R
    print(P)