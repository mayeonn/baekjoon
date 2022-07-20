import sys
C = int(input())

for i in range(C):
    num = 0
    scores = list(map(int, sys.stdin.readline().split()))
    avg = sum(scores[1:])/scores[0]
    for i in scores[1:]:
        if i > avg: num+=1
    score = round(num/scores[0]*100, 3)
    print(f"{score:.3f}%")