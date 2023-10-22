import sys
input = sys.stdin.readline
H, W, N = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]
result = 0

div = []
coordinate = []
for i in range(0, N//2+1):
    if N%(i+1) == 0:
        if i+1 <= W and N//(i+1) <= H:
            div.append([i+1, N//(i+1)])

for d in div:
    w = d[0]
    h = d[1]
    arr = [[y, x, y+h, x+w] for x in range(W-w+1) for y in range(H-h+1)]
    coordinate.extend(arr)

if len(coordinate)==0:
    print(-1)
else:
    for i in coordinate:
        arr = [S[n][m] for m in range(i[1], i[3]) for n in range(i[0], i[2])]
        result = max(result, max(arr) - min(arr))
    print(result)