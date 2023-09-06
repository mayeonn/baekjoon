n = int(input())
stairs = []
dp = []

for _ in range(n):
    stairs.append(int(input()))

if n==1:
    print(stairs[0])
elif n==2:
    print(stairs[0]+stairs[1])
else:    
    dp.append(stairs[0])
    dp.append(stairs[0]+stairs[1])
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

    for i in range(3, n):
        dp.append(
            max(dp[i-2] + stairs[i], 
                dp[i-3] + stairs[i-1] + stairs[i])
            )

    print(dp[n-1])
