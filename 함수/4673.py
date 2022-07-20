def d(n):
    for i in str(n):
        n+=int(i)
    return n

arr = list(range(1, 10001))
remove_arr = []

for num in arr:
    if d(num) <= 10000:
        remove_arr.append(d(num))

for num in set(remove_arr):
    arr.remove(num)

for i in arr:
    print(i)