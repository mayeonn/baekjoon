def numExecution(n):
    x = 0
    for i in range(1,n):
        x += (n-i)
    return x

n = int(input())
print(numExecution(n))
print(2)    #O(n^2) 
