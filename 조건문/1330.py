text = input().split()
A = int(text[0])
B = int(text[1])
if  A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")