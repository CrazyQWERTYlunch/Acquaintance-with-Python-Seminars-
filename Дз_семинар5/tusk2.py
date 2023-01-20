"""Задача 2. Создайте программу для игры с конфетами человек против человека.

 Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
 Все конфеты оппонента достаются сделавшему последний ход.
 Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом" """

from random import randint

def move_player(name_player, candies, max_move):
    valid = False
    while not valid:
        move = input(f'{name_player}, Ваш ход... ')
        try:
            move = int(move)
            if move > 0 and move <= max_move and move <= candies:
                print(f'Вы забрали {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                valid = True
            else:
                print(f'Количество взятых конфет должно быть в интервале от 1 до {max_move} или не больше оставшегося количества конфет')
        except:
            print('Необходимо ввести целое число.')
    return candies

def move_stupid_bot(candies, max_move):
    move = randint(1, max_move) if candies >= max_move else randint(1, candies)
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

def move_smart_bot(candies, max_move):
    move = candies % (max_move + 1)
    if move == 0:
        move = randint(1, max_move) if candies >= max_move else candies
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

def check_win(candies, determing_moves, first_name, second_name):
    if candies == 0:
        return first_name if determing_moves % 2 == 0 else second_name
    else:
        return False





def player_vs_stupid_bot ():
    name_player = input('Введите свое имя: ')
    candies = 2021
    max_move = 28
    count_for_check_win = candies // max_move
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = move_player(name_player, candies, max_move)
        else:
            candies = move_stupid_bot(candies, max_move)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def player_vs_smart_bot ():
    name_player = input('Введите свое имя: ')
    candies = 2021
    max_move = 28
    count_for_check_win = candies // max_move
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = move_player(name_player, candies, max_move)
        else:
            candies = move_smart_bot(candies, max_move)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def player_vs_player ():
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')
    candies = 2021
    max_move = 28
    count_for_check_win = candies // max_move
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = move_player(name_first_player, candies, max_move)
        else:
            candies = move_player(name_second_player, candies, max_move)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(candies, determing_moves, name_first_player, name_second_player)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        determing_moves += 1

def main():
    type_game = input('Введите 1, если хотите играть с другим игроком, и любую другую цифру, если с ботом: ')
    if (type_game == '1'):
        player_vs_player()
    else:
        bot_game = input('Введите 0, если хотите играть с глупым ботом, и любую другую цифру, если с умным: ')
        if bot_game == '0':
            player_vs_stupid_bot ()
        else:
            player_vs_smart_bot ()
main()