numbers = str( input( '' ) )
split_numbers = numbers.split()
a = list( map( int, split_numbers ) )
a = a[:3]
sort_numbers = sorted( a )
for i in sort_numbers:
    print( i )
print( '' )
for i in a:
    print( i )
