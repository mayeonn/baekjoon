T = int(input())
arr = []

for i in range(T):
    arr.append(input())

for i in range(T):
    for _ in range(25):
        arr[i] = arr[i].replace("()", "")
        if len(arr[i])==0:
            print('YES')
            break
    if len(arr[i])!=0:
        print('NO')