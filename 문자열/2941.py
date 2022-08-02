alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in alphabet:
    a = a.replace(i, '*')
print(len(a))