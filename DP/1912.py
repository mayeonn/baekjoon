# '연속된' 수의 합이기 때문에 모든 합의 경우를 생각할 필요 없다.
# 연속된 수의 합은 반복 계산이 발생하지 않도록 주의해야 한다.

# range(1, n)에서 이전 값과 연속할지 결정하여 합의 최대값을 기록하고
# 그 중 최대값을 꺼낸다.
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    m[i] = max(m[i], m[i]+m[i-1])

print(max(arr))