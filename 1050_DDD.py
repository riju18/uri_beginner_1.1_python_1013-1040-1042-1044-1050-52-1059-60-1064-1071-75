code = int(input('enter code: '))

ddd = {
    61: 'brasilia',
    71: 'salvador',
    11: 'Sao Paulo',
    21: 'Reo de Jeneiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Victoria',
    31:'Belo Horizonte'
}

for i in ddd:
    if code in ddd:
        print(ddd[code])
        break
    else:
        print('DDD nao cadastrado')
        break
