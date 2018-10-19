line = str(input("enter numbers: "))
split = line.split()
a, b, c = list(map(int, split))
maiorAB = ((a + b) + abs(a-b))/2
maiorAC = ((a + c) + abs(a-c))/2
maior = ((maiorAB + maiorAC) + abs(maiorAB-maiorAC))/2
print("%d eh o maior" % maior)
