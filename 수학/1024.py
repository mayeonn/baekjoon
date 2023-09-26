N, L = map(int, input().split())
x = range(0)
isThere = False
# 합이 N이면서, 길이가 적어도 L인

for len in range(L, 101):
    min = N/len - (len+1)/2 + 1
    if int(min)==min and min >= 0:
        for i in range(int(min), int(min)+len):
            isThere = True
            print(i, end=" ")
        break
if isThere==False:
    print(-1)