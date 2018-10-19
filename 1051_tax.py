tax = str(input('enter amount: '))
tax = round(float(tax), 2)
if tax >= 0 and tax <= 2000:
    print('Isento')
elif tax > 2000 and tax <= 3000:
    ran = tax - 1000
    newTax = (ran * 8) / 100
    print(newTax)
elif tax > 3000 and tax <= 4500:
    preTax = (1000 * 8) / 100
    extraTax = ((tax % 3000) * 18) / 100
    newTax = preTax + extraTax
    print('R$ ',newTax)
elif tax > 4500:
    preTax = (1000 * 8) / 100
    postTax = (1500 * 18) / 100
    extraTax = ((tax % 1500) * 28) / 100
    newTax = preTax + postTax + extraTax
    print('R$ {0:.2f}'.format(newTax))
    

        
