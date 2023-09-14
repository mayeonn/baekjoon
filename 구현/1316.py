import sys
N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    word = sys.stdin.readline()
    isGroupWord = True

    for x in word:
        word = word.replace(x+x, x)

    for i in range(len(word)):
        if word.find(word[i], i+1)!=-1:
            isGroupWord = False
            break
    
    if isGroupWord:
        cnt+=1

print(cnt)