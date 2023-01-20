"""Задача 3. Создайте программу для игры в ""Крестики-нолики""."""
# from random import randint
# def print_board(board): # Демонстрация игрового поля
#     for i in range(3):
#         for j in range(3):
#             print(f"|{board[3*i+j]}", sep="", end="")
#         print('|')
#
# # def coin_flip(name_player1,name_player2): # TODO:
# #     print("Чтобы определить кто ходит первым бросим монетку")
# #     answer = int(input("Выберите сторону монетки: \n 1. Орел \n 2. Решка\n"))
# #     if answer == randint(1,2): return name_player1
# #     else: return name_player2
#
#
# def step_player(board,player,symbol):
#     step = int(input(f"{player} укажите поле для своего хода: "))
#     # step_check = False
#     # while step not in board: # Строка не выходит из цикла...решить
#     #     step = input("Данный ход совершить невозможно, пожалуйста выберите другое поле: ")
#     board[step-1] = symbol
#     return board
#
#
#
# def check_victory(board):
#     if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
#     board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or \
#     board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
#         return True
#
#
#
# def game(name_player1, name_player2):
#
#     turn = name_player1
#     board = [i for i in range(1,10)] # генератор поля
#     game_progress = 0 # этап игры
#     end = False # закончилась ли игра
#     winner = ""
#     while not end:
#         print_board(board)
#
#         if turn == name_player1:
#             player = name_player1
#             symbol = "X"
#         else:
#             player = name_player2
#             symbol = "O"
#
#         board = step_player(board,player,symbol)
#
#
#         game_progress +=1
#
#         if game_progress > 4:
#             end = check_victory(board)
#             winner = turn
#         elif game_progress >= 9:
#             end = True
#             winner = "Ничья"
#
#         if turn == name_player1: # передача хода
#             turn = name_player2
#         else: turn = name_player1
#     print_board(board)
#     return winner
#
#
# def main():
#     name_player1 = input("Введите имя первого игрока: ")
#     name_player2 = input("Введите имя второго игрока: ")
#     winnner = game(name_player1, name_player2)
#     print(f"Победил {winnner}")
#
#
#
# main()