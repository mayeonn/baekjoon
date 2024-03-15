import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())*-1
    if x==0:
        print(hq.heappop(heap)*-1 if heap else 0)  #ternary operator
    else:
        hq.heappush(heap, x)

