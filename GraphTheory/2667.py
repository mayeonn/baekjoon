N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = []

def dfs(x, y, cnt):
    graph[x][y] = 0 #방문

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny]==1:
            cnt = dfs(nx, ny, cnt+1)
    return cnt  # 단지 내 집의 수 반환

# 단지 시작점 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            count.append(dfs(i, j, cnt = 1))

count.sort()
print(len(count))
for i in count:
    print(i)