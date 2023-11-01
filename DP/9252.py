import sys

str1 = list(sys.stdin.readline())
str2 = list(sys.stdin.readline())

dp = [[""]*len(str2)]*len(str1)

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        # dp[i][j] : str1의 i번쨰까지, str2의 j번째까지 문자열의 LCS
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        
        elif len(dp[i-1][j]) >= len(dp[i][j-1]):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]
    # print(dp[i])

result = dp[-1][-1]
print(len(result))
if len(result)!=0:
    print(result)