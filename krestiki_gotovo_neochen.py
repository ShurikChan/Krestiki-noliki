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

def correct_move(position):
    if position < 1 or position > len(board):
        print("Некорректный ход, выбирайте от 1 до 9")
        return False
    if board[i] != ' ':                                   #Тут нужна помощь
        print("Клетка занята, выберите другую!")
        return False
    return True
   
def players_do_moves():
    while True:
        make_move('X', int(input(f'{first_plr} {choice}: ')))
        make_move('O', int(input(f'{second_plr} {choice}: ')))
        if correct_move(position):
            return position                               #Тут нужна помощь
        