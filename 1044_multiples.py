numbers = str(input(''))
split = numbers.split()
a, b = list(map(int, split))
if b % a == 0:
    print('Sao Multiplos\n')
else:
    print('Nao sao Multiplos\n')
