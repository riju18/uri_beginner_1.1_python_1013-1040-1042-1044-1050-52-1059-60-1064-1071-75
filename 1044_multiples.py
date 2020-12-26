numbers = str( input( '' ) )
split_numbers = numbers.split()
a = list( map( int, split_numbers ) )[:2]
x = a[0]
y = a[1]
if x != 0:
    if y % x == 0 or x % y == 0:
        print( 'Sao Multiplos' )
    else:
        print( 'Nao sao Multiplos' )
