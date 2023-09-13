import sys
n = int(sys.stdin.readline())
seq = []
answer = []
stack = []
isPossible = True
i = 0 # seq index
j = 1 # push number

for _ in range(n):
    seq.append(int(sys.stdin.readline()))

while i<n:
    if j > seq[i]:
        if(stack.pop()!=seq[i]):
            isPossible = False
            break
        answer.append(0)
        i+=1
    else:
        stack.append(j)
        j+=1
        answer.append(1)

if isPossible: 
    for x in answer:
        if x==0:
            print('-')
        else:
            print('+')
else:
    print("NO")