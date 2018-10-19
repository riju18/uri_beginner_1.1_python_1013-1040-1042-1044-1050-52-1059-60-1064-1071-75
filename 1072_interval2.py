import numpy as np

n = int(input('number of testcase: '))
numbers = []
betnRange = []
outOfRange = []
for i in range(n):
    numbers.append(int(input()))

# numberRange = np.arange(10, 20)

for i in numbers:
    if i in range(10, 21):
        betnRange.append(i)
    else:
        outOfRange.append(i)    

print('in range(10-20):', betnRange)
print('out of range: ', outOfRange)