cycle = 0
N = previous = int(input())

while True:
    a = (previous%10)
    b =  int(previous/10) + a
    new = (a%10)*10 + b%10
    cycle+=1
    previous = new
    if(new==N): break
print(cycle)