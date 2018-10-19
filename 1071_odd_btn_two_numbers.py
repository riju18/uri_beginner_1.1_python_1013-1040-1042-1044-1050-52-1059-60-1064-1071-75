import numpy as np

numbers = str(input(''))
split = numbers.split()
a, b = list(map(int, split))
allNum = np.arange(a, b, -1)
count = 0
for i in allNum:
    if i % 2 != 0:
        count += 1
print(count)        