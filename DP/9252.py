from itertools import combinations

str1 = list(input().rstrip())
str2 = input().rstrip()
result = ""

for i in range(len(str1), 0, -1):
    dp = list(combinations(str1, i))
    for string in dp:
        LCS = ""
        temp = str2
        for letter in string:
            idx = temp.find(letter)
            if idx == -1:
                break
            else:
                temp = temp[idx+1:]
                LCS += letter
        if len(LCS)==len(string):
            result = LCS
            break
    if len(result) != 0:
        break

print(len(result))
if len(result) != 0:
    print(result)