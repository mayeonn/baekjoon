import sys
# numpy 사용하지 않기 (runtime error!)

def multiplyMatrix(m1, m2):
    length = len(m1)
    result = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += m1[i][k]*m2[k][j]
                result[i][j] %= 1000    # 큰 수 연산 줄이기
    return result

def recursivelyMultiplying(m, n):
    if n==1:
        return m
    else:
        # n이 짝수이면,  m^n 을 (m^2)^n/2 로 바꾸어 m을 제곱하고 n을 2로 나눔
        if n%2==0:
            m = recursivelyMultiplying(m, n//2)
            return multiplyMatrix(m, m)
        # n이 홀수이면,  m^n 을 m^(n-1) * A 로 바꾸어 m을 제곱
        else:
            m = recursivelyMultiplying(m, n-1)
            return multiplyMatrix(A, m)


N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = recursivelyMultiplying(A, B)

for i in range(N):
    for j in range(N):
        print(result[i][j]%1000, end=' ')
    print()