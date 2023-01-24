import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

# 반복문 사용은 시간 초과
# V/(A-B)는 정상에 도달하면 미끄러지지 않는다는 조건을 무시
day = (V-B)/(A-B)

# ceil: 올림, floor: 내림
print(math.ceil(day))