import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
x = y = 0
queue = deque()
queue.append((x,y))

while queue:
    x, y = queue.popleft()  # 인접한 것부터 검사(BFS)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and maze[nx][ny]==1:
            queue.append((nx, ny))  # 가능한 건 queue에 넣고
            maze[nx][ny] = maze[x][y] + 1   # 이동 칸 수 기록
print(maze[N-1][M-1])
    