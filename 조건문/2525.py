hour, minute = map(int, input().split())
require = int(input())
minute += require
if minute >= 60:
    hour += int(minute/60)
    minute %= 60
    if hour>=24:
        hour-=24
print(hour, minute)