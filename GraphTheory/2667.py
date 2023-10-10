graph = []

N = int(input())
for _ in range(N):
    graph.append(list(map(int, input())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    
    if graph[x][y]==1:
        global count
        count+=1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny) # 사방으로 호출
        return True
    return False

count = 0   
num = []    # 단지내 집의 수
result = 0  # 단지 수

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            num.append(count)
            result += 1
            count = 0

print(result)

num.sort()
for i in num:
    print(i)