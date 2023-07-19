N = int(input())
groupWord = 0

for i in range(N):
    a = input()
    alphabet = []
    for j in range(len(a)):
        if(a[j] not in alphabet):
            if(j==len(a)-1):
                groupWord += 1
            else:
                alphabet.append(a[j])
        elif(a[j] != alphabet[len(alphabet)-1]):
            break
        else:
            groupWord += 1
            break
print(groupWord)