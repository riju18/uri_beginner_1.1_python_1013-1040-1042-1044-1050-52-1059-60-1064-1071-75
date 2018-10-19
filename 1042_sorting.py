numbers = str(input(''))
split = numbers.split()
a = list(map(int, split))
sortt = sorted(a)
for i in sortt:
    print(i)
print('\n')
for i in a:
    print(i)