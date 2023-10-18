import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
for _ in range(N):
    tp = list(map(int, input().split()))
    T.append(tp[0])
    P.append(tp[1])

dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if N-i < T[i]:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])

print(dp[0])