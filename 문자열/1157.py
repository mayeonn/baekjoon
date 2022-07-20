W = input().upper()
words = list(set(W))
cnt = []

for i in words:
    cnt.append(W.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(words[cnt.index(max(cnt))])