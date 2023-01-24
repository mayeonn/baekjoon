X = int(input())

line = 1 #몇 번째 줄인지
cnt = 1 #몇 번째 분수

while X > cnt:
    line += 1
    cnt += line

cnt = cnt - line + 1
if(line%2==0):
    x = 1
    y = line
    while X > cnt:
        x+=1
        y-=1
        cnt+=1
else:
    x = line
    y = 1
    while X > cnt:
        x-=1
        y+=1
        cnt+=1

print("%d/%d" % (x, y))