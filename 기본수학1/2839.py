sugar = int(input())
bag = 0

while sugar >= 0:
    if(sugar%5 == 0):   # sugar가 5의 배수일 때 (0인 경우 포함)
        bag += sugar//5
        print(bag)
        break
    else:
        sugar -= 3
        bag += 1
else:   # while의 else문 : while 조건식이 거짓으로 판정되어 실행문들이 수행되지 않을 경우에 수행될 내용
    print(-1)