import sys
a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

fn0 = a1*n0 + a0

# c*g(n) = c*n
# f(n)이 c*g(n) 보다 같거나 작으려면 
# 기울기가 같거나 작아야 하고, (a1 <= c)
# 가장 왼쪽 값인 n0에서 같거나 작은지 확인한다.
if a1<=c and fn0 <= c*n0:
    print(1)
else:
    print(0)