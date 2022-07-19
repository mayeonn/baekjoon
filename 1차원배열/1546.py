import sys
N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max_s = max(scores)
for i in range(N):
    scores[i] = scores[i]/max_s*100
print(sum(scores, 0.0)/N)