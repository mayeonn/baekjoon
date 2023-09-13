import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque([i for i in range(1, N+1)])

while True:
    # deq.popleft()
    if len(deq)==1:
        print(deq.pop())
        break
    deq.popleft()
    temp = deq.popleft()
    deq.append(temp)
