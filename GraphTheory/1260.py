from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visitedDFS = [False]*(N+1)
visitedBFS = [False]*(N+1)

def dfs(v):
    visitedDFS[v] = True
    print(v, end=" ")
    for i in range(1, N+1):
        if graph[v][i] and not visitedDFS[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visitedBFS[v] = True
    while q:
        v = q.popleft() 
        print(v, end = " ")
        for i in range(1, N+1):
            if graph[v][i] and not visitedBFS[i]:
                q.append(i)
                visitedBFS[i] = True

dfs(V)
print()
bfs(V)
