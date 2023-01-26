# 시간초과
"""
def isPrimeNum(x):
    if x==1:
            return False
    for i in range(2,x):
        if x%i==0: 
            return False
    return True

M, N = map(int, input().split())

for x in range(M,N+1):
    if isPrimeNum(x):
        print(x)
"""
# 효율적으로 약수 찾기
'''
N의 약수를 구할 때는, 1부터 N의 제곱근 까지의 수만 확인하면 된다
'''
# 에라토스테네스의 체
'''
검증하고자 하는 수의 제곱근까지만을 소수인지 판별 -> 대량의 소수를 한번에 판별할 때 속도가 빨라 유용함

알고리즘
1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.

2. 2는 소수이므로 2를 쓴다.
3. 자기 자신을 제외한 2의 배수를 모두 지운다.

4. 남아있는 수 가운데 3은 소수이므로 3을 쓴다.
5. 자기 자신을 제외한 3의 배수를 모두 지운다.

6. 남아있는 수 가운데 5는 소수이므로 5를 쓴다.
7. 자기 자신을 제외한 5의 배수를 모두 지운다.

8. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
'''

M, N = map(int, input().split())

# init list
sieve = [True]*(N+1)
sieve[1] = False

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
for i in range(2, int(N**0.5) + 1): 
    if sieve[i] == True:    
        # i가 소수인 경우 i 이후 i의 배수들에 False
        for j in range(i+i, N+1, i):
            sieve[j] = False

for i in range(M, N+1):
    if sieve[i]:
        print(i)
