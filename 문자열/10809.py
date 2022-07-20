S = input()
result = [-1]*26
order = 0
for i in S:
    if(result[ord(i)-97]==-1):
        result[ord(i)-97] = order
    order+=1
print(*result)