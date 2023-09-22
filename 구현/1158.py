N, K = map(int, input().split())
arr = [i+1 for i in range(N)]

answer = []
index = 0

for i in range(N):
    index += K -1
    if index >= len(arr):
        index = index%len(arr)
    answer.append(arr.pop(index))

print(str(answer).replace('[', '<').replace(']', '>'))