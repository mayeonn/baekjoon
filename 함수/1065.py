def hansu(n):
    if n<100: 
        return True
    n = str(n)
    if(int(n[1])-int(n[0]) == int(n[2])-int(n[1])): 
        return True
    return False

cnt = 0
N = int(input())
for i in range(1, N+1):
    if(hansu(i)): 
        cnt+=1
print(cnt)