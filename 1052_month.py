month = int(input('month number: '))

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

for i in months:
    if month in months:
        print(months[month])
        break
    else:
        print('error')
