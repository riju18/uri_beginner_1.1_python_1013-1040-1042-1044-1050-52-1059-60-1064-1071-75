number = int(input('enter number: '))
allNUm = []
for i in range(number):
    allNUm.append(input())
allInt = list(map(int, allNUm))
for i in allInt:
    if i < 0 and i % 2 != 0:
        print('ODD NEGATIVE')
        continue
    elif i == 0:
        print('NULL')
        continue
    elif i > 0 and i % 2 != 0:
        print('ODD POSTIVE')
        continue
    elif i > 0 and i % 2 == 0:
        print('EVEN POSTIVE')
        continue
    elif i < 0 and i % 2 == 0:
        print('EVEN NEGATIVE')
        continue

