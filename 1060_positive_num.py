
x = []
for i in range(6):
    x.append(input())

x = list(map(float, x))
count = 0
for i in x:
    if i > 0:
        count += 1

print('{} valores positivos'.format(count))

