

row1 = ['▥', '▥', '▥']
row2 = ['▥', '▥', '▥']
row3 = ['▥', '▥', '▥']

column = ['A', 'B', 'C']
map = [row1, row2, row3]

treasure_vault = input('Where do you want to keep your treasure? ').upper()

column_index = treasure_vault[0]

column_position = column.index(column_index)
row_position = int(treasure_vault[-1])

map[column_position][row_position-1] = 'X'


print(f'Hiding your treasure, X marks the spot.\n{row1}\n{row2}\n{row3}')


"Alternative approach"

if treasure_vault[0] == 'A':
    row1[row_position-1] = "X"
elif treasure_vault[0] == 'B':
    row2[row_position-1] = "X"
else:
    row3[row_position-1] = "X"


if treasure_vault in ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"):
    print(f'Alternative result:\nHiding your treasure, X marks the spot.\n{
          row1}\n{row2}\n{row3}')
else:
    print('Enter a valid vault number. Available vault: \nA1, A2, A3, B1, B2, B3, C1, C2, C3.')
