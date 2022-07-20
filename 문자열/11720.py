import sys
N = input()
nums = sys.stdin.readline().strip()
sum = 0
for i in nums:
    sum+=int(i)
print(sum)