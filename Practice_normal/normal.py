d = {'Pixel 2': '399',
        'One Plus 6T': '429', 'iPhone XR': '499',
        'One Plus 7': '499', 'iPhone XS': '549', 'iPhone 11': '599',
        'Pixel 3': '599', 'One Plus 7T': '599', 'iPhone XS Max': '649',
     'iPhone 12 Mini': '699', 'iPhone 11 Pro': '699', 'Galaxy S9': '699',
     'iPhone 12': '799', 'One Plus 8': '799', 'Galaxy S10': '899', 'Pixel 4': '899',
     'One Plus 8T': '899', 'One Plus 8 Pro': '899', 'iPhone 12 Pro': '999', 'Galaxy S20': '999',
        'Galaxy Note 20': '999', 'iPhone 12 Pro Max': '1099', 'Galaxy S20+': '1199',
        'Galaxy Note 20 Ultra': '1299',
     'Galaxy S20 Ultra': '1399'}

for k, v in d.items():
    if k == 'Pixel 2' or k == 'Galaxy S20 Ultra':
        if k == 'Pixel 2':
            print("The least product name is :",k, "and it's price is:",v)
        else:
            print("The highest product name is :",k, "and it's price is:",v)

least_flight_a = 10
to_enter = [least_flight_a]

print("the value is :",to_enter)
