

row1 = ['▥', '▥', '▥']
row2 = ['▥', '▥', '▥']
row3 = ['▥', '▥', '▥']

row = [row1, row2, row3]

treasure_vault = input('Where do you want to keep your treasure? ')

column = int(treasure_vault[-1])

if treasure_vault[0] == 'A':
    row1[column-1] = "X"
elif treasure_vault[0] == 'B':
    row2[column-1] = "X"
else:
    row3[column-1] = "X"


if treasure_vault in ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'):
    print(f'Hiding your treasure, X marks the spot.\n{row1}\n{row2}\n{row3}')
else:
    print('Enter a valid vault number. Available vault: \nA1, A2, A3, B1, B2, B3, C1, C2, C3.')
