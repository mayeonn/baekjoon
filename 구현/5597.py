d = [0]*31
d[0] = 1

for _ in range(28):
    i = int(input())
    d[i] = 1

for i, j in enumerate(d):
    if j==0:
        print(i)