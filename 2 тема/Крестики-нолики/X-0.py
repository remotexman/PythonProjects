def check_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'

    if area[0][0] == 'O' and area[0][1] == 'O' and area[0][2] == 'O':
        return 'O'
    if area[1][0] == 'O' and area[1][1] == 'O' and area[1][2] == 'O':
        return 'O'
    if area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][0] == 'O' and area[1][0] == 'O' and area[2][0] == 'O':
        return 'O'
    if area[0][1] == 'O' and area[1][1] == 'O' and area[1][2] == 'O':
        return 'O'
    if area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][1] == 'O' and area[2][0] == 'O':
        return 'O'
    return '*'


print('Это игра "крестики-нолики"')
print('Первыми ходят крестики')
print('________________________________')

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
def draw_area():
    for i in area:
        print(*i)
    print()

def identify_rows_and_colums():
    rows = int(input('Введите номер строки (1, 2, 3): ')) - 1
    columns = int(input('Введите номер столбца (1, 2, 3): ')) - 1
    return rows, columns

def check(row, column):
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print()
        print('Попробуйте еще раз')
        check(*identify_rows_and_colums())

for turn in range(1, 10):
    print(f'Ход {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    check(*identify_rows_and_colums())
    draw_area()

    winner = check_winner()
    if winner == 'X':
        print('Победили крестики')
        break
    elif winner == '*' and turn == 9:
        print('Ничья')
        break
    elif winner == 'O':
        print('Победили нолики')
        break

