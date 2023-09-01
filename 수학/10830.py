import numpy as np

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


# 행렬 곱셈
def mul_matrix(matrix1, matrix2):
    # 0으로 채운 N*N 행렬 초기 생성
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix1[i][k] * matrix2[k][j] % 1000
    return result


# 행렬 A를 B제곱  -  행렬 곱셈을 반복(거듭제곱을 반복)
"""
B가 4(짝수)인 경우, 
    AAAA = (A^2)^2 = A^(B//2)
B가 5(홀수)인 경우, A를 한번 더 곱함
    AAAAA = ((A^2)^2)A = A^(B//2 + 1)
"""
def square(a, b):
    if b==1:    # b가 1이 될 때까지 재귀
        return a
    else:
        tmp = square(a, b//2)

        if b%2==0:  # b가 짝수인 경우
            return mul_matrix(tmp, tmp)
        else:  # b가 홀수인 경우
            return mul_matrix(mul_matrix(tmp, tmp), a)



result = square(A, B)

for row in result:
    for col in row:
        print(col%1000, end=" ")
    print()