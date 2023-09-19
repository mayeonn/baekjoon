import sys
cnt = 0
n = int(sys.stdin.readline())

# 중첩 반복문은 시간 복잡도를 증가시킨다. 반복문을 분석해 식 찾기.
for i in range(1, n):
    cnt += i*(i-1)//2

print(cnt)
print(3)