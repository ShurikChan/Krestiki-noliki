board = [' '] * 9
first_plr = input("Введите имя первого игрока: ")
second_plr = input("Введите имя второго игрока: ")
choice = "выбирает клетку"


def print_board():
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])

def make_move(marker, position):
    board[position] = marker
print(board)

make_move('X', int(input(f'{first_plr} {choice}: ')))
print_board()
make_move('O', int(input(f'{second_plr} {choice}: ')))
print_board()
make_move('X', int(input(f'{first_plr} {choice}: ')))
print_board()
make_move('O', int(input(f'{second_plr} {choice}: ')))
print_board()
make_move('X', int(input(f'{first_plr} {choice}: ')))
print_board()
make_move('O', int(input(f'{second_plr} {choice}: ')))
print_board()
make_move('X', int(input(f'{first_plr} {choice}: ')))
print_board()
make_move('O', int(input(f'{second_plr} {choice}: ')))
print_board()
make_move('X', int(input(f'{first_plr} {choice}: ')))
print_board()
