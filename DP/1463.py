N = int(input())
dp = [0]*(N+1)

# index 1부터 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # -1
    # dp[4]이면 dp[2] 값을 사용
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])