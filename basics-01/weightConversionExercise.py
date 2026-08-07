#Python weight converter.


weight = float(input('Enter your weight: '))
unit = input('Kilograms or pounds?(K or L): ').upper() 
# upper() => (K == k)

if unit == 'K':
    # weight = weight * 2.205
    weight *= 2.205 
    unit = 'Lbs.'
    print(f'your weight is :{weight} {unit}')
elif unit == 'L':
    # weight = weight / 2.205
    weight /= 2.205
    unit = 'Kgs.'
    print(f'Weight is : {weight} {unit}')
else:
    print(f'{unit} was not valid .')
