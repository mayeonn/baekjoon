import math
N, M = map(int, input().split())

# 내장함수 math.gcd : 최대공약수(Greatest Common Divisor)
print(math.gcd(N, M))
# 내장함수 math.lcm : 최소공배수(Least Common Multiple)
print(math.lcm(N, M))