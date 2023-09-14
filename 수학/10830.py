import sys
# numpy 사용하지 않기 (시간초과)

def multiplyMatrix(m1, m2):
    length = len(m1)
    result = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += m1[i][k]*m2[k][j]
                result[i][j] %= 1000    # 큰 수 연산 줄이기
    return result

def recursivelyMultiplying(matrix, b):
    if b==1:
        return matrix
    else:
        # B가 짝수면  A^n 을 (A^2)^n/2 로 바꾸어  A를 곱하고, N을 2로 나눈다
        if b%2==0:
            matrix = recursivelyMultiplying(matrix, b//2)
            return multiplyMatrix(matrix, matrix)
        # B가 홀수면 A^n 을 A^(n-1) * A 로 바꾸고 result에 A를 곱한다.
        else:
            matrix = recursivelyMultiplying(matrix, b-1)
            return multiplyMatrix(A, matrix)


N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = recursivelyMultiplying(A, B)

for i in range(N):
    for j in range(N):
        print(result[i][j]%1000, end=' ')
    print()