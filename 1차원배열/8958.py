import sys

N = int(input())
cases = []

for i in range(N):
    score=0
    continuity = 0
    cases = list(sys.stdin.readline().strip())
    for j in range (len(cases)):
        if(cases[j]=='X'):
            continuity = 0
        else:
            continuity+=1
        score+=continuity
    cases.clear()
    print(score)