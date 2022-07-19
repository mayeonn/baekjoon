arr = [0]*10
val = 1

for i in range(3):
    val *= int(input())
ABC = list(format(val))

for i in range(len(ABC)):
    arr[int(ABC[i])]+=1

for i in range(10):
    print(arr[i])