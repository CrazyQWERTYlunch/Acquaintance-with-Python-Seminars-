import pygame
import sys


def check_win(mas,sign):
    check_moves = 0
    for row in mas:
        check_moves += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == mas[1][col] == mas[2][col] == sign:
            return sign
    if mas[0][0] == mas[1][1] == mas[2][2] == sign or \
        mas[0][2] == mas[1][1] == mas[2][0] == sign:
        return sign
    if check_moves == 0:
        return 'Draw'
    return False

def print_win(winner):
    screen.fill(black)
    font = pygame.font.SysFont('domestic manners', 450)
    text = font.render(game_over, True, white)
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x,text_y])



pygame.init()

size_block = 100
margin = 20
width = height = size_block*3+margin*4

size_window = (width,height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Поле для игры в крестики-нолики")
black = (0,0,0)
deeppink = (255,20,147)
lime = (0,255,0)
white = (255,255,255)
mas = [[0]*3 for i in range(3)]
turn_of_move = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            row = x_mouse // (size_block+margin)
            col  = y_mouse // (size_block+margin)

            if mas[row][col] == 0:
                if turn_of_move % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                turn_of_move += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            turn_of_move = 0
            screen.fill(black)
    # if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = deeppink
                elif mas[row][col] == 'o':
                    color = lime
                else:
                    color = white
                x = row*size_block + (row+1) * margin
                y = col * size_block + (col + 1) * margin
                pygame.draw.rect(screen,color, (x,y,size_block,size_block))

                if color == deeppink:
                    pygame.draw.line(screen,white,(x+5,y+5),(x+size_block-5,y+size_block-5),9)
                    pygame.draw.line(screen, white, (x+size_block-5, y+5), (x+5, y + size_block-5), 9)
                elif color == lime:
                    pygame.draw.circle(screen,white,(x+size_block//2, y+size_block//2),size_block//2-3, 9)
    if (turn_of_move-1) % 2 == 0:
        game_over = check_win(mas,'x')
    else:
        game_over = check_win(mas,'o')


# Вывод победителя
    if game_over:
        print_win(game_over)

    pygame.display.update()


# TODO: Прописать бота
