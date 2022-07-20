def d(n):
    for i in str(n):
        n+=int(i)
    return n

numbers = set(range(1, 10001))
remove_numbers = set()

for n in numbers:
    remove_numbers.add(d(n))

self_num = sorted(numbers - remove_numbers)
for i in self_num:
    print(i)