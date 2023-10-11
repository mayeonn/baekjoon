from collections import deque

N, K = map(int, input().split())
queue = deque([x for x in range(1, N+1)])
cnt = 0
result = []

while queue:
    cnt += 1
    x = queue.popleft()
    if cnt%K==0:
        result.append(x)
    else:
        queue.append(x)
 
print(str(result).replace("[", "<").replace("]", ">"))
