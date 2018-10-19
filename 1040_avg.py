scores = str(input(''))
retake = str(input(''))
split = scores.split()
a, b, c, d = list(map(float, split))
a = round(a, 1)
b = round(b, 1)
c = round(c, 1)
d = round(d, 1)
retake = round(float(retake), 1)
media = (a + b + c + d) / 4
print('Media: {}'.format(round(media, 1)))
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 and media < 7:
    print('Aluno em exame.')
print('Nota do exame: {}'.format(retake))
finalAvg = (media + retake) / 2
if finalAvg >= 5:
    print('Aluno aprovado.')
elif finalAvg < 5:
    print('Aluno reprovado.')
print('Media final: {}'.format(round(finalAvg, 1)))
