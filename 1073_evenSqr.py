number = int(input('enter a number: '))
allEven = []

if number >= 5 and number <= 2000:
       for i in range(1, number + 1):
                if i % 2 == 0:
                        allEven.append(i)
                        
for i in allEven:
    print(i,'^','2',' = ',i**2)
