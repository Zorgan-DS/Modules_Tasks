board = list(range(1, 10)) # Глобальная переменная (состояние поля)

def draw_board(board): # рисуем поле для игры
    print('-'*13)
    for i in range(3): # начиная с i = 0
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|' )
        print('-'*13)

def take_input(play_token): # записывается буква текущего хода (X или O)
    valid = False # отвечает за разблокировку/блокировку цикла
    while not valid: 
        player_answer = input('Куда будем ставить ' + play_token + '?\n>') # Ввод пользователя
        try: # ставим условие ввода только цифр (не букв)
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод!')
            continue
        if player_answer >= 1 and player_answer <= 9: # ставим условие ввода цифр от 1 до 9
            if (str(board[player_answer - 1])) not in 'XO': # занято ли место,куда игрок ставит Х или О
                board[player_answer - 1] = play_token # если не занято, то меняем состояние доски
                valid = True # блокируем цикл
            else:
                print('Клетка занята')
        else:
            print('Ошибка при вводе, введите число от 1 до 9')

def check_win(board): # проверка выигрышных координат (индексы списка в кортежах)
    win_tuple = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_tuple:
        if board[each[0]] == board[each[1]] == board[each[2]]: # сравниванием совпдение по каждому each
            return board[each[0]]
    return False

def main(board): # вызываем исполнение функции
    counter = 0 # считает ходы
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)

main(board)