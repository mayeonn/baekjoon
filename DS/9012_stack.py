"""
'('일 때 : stack에 PUSH

')'일 때 
stack이 비어있지 않다면 POP
stack이 비어있으면 print("NO")

문자열 확인이 끝났을 때
stack이 비어있지 않다면 print("NO")
stack이 비어있으면 print("YES")
"""

T = int(input())

for _ in range(T):
    stack = []
    string = input()
    isVPS = True

    for x in string:
        if x=='(':
            stack.append(x)
        else:
            if not stack:
                isVPS = False
                break
            else:
                stack.pop()

    if not stack and isVPS:
        print("YES")
    else:
        print("NO")
