T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층 n호까지 채워넣기
    f0 = [x for x in range(1, n+1)]

    # k층까지 f0 새로 채우기 반복
    for k in range(k):
        for i in range(1, n):
            f0[i] += f0[i-1]    #밑 층과 옆 집 수 더하기
    
    print(f0[n-1])