import sys
import math

T = int(input())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    floor = H if N%H == 0 else N%H
    print("%d%s" % (floor, format(math.ceil(N/H), '02')))