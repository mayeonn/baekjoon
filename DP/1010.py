import sys
T = int(sys.stdin.readline())
dp = [[i]*30 for i in range(30)]
dp[1] = [i for i in range(30)]

for i in range(1, 30):
    for j in range(1, i+1):
        if i==1 or j==1:
            continue
        elif i==j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            dp[j][i] = dp[i][j]

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(dp[N][M])
