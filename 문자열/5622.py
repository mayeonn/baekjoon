dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
min = 0
for i in a:
    for j in dial:
        if(i in j):
            min += dial.index(j)+3
print(min)