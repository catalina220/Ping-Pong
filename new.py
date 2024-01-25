import pygame
import sys
import random
import time


pygame.init()

# параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('PING PONG')

# цвета
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


# функция для отображения текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, False, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# функция записи в файл
def write_to_file(file, text):
    with open(file, 'w') as f:
        f.write(str(text))

# функция для отображения стартового окна
def start_screen():

    #Загрузка изображений
    background = pygame.image.load('start.png')
    background = pygame.transform.scale(background, (800, 600))

    label_image = pygame.image.load('label_1.png')
    label_image = pygame.transform.scale(label_image, (550, 160))

    start_button = pygame.Rect(320, 520, 150, 50)

    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Действия клавиатуры и мышки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    register_screen()

        #Позиция мышки
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if start_button.collidepoint(mouse_x, mouse_y):
            button_color = green
        else:
            button_color = black

        #Отображение на экран
        pygame.draw.rect(screen, button_color, start_button)
        draw_text('Start', pygame.font.Font('freesansbold.ttf', 30), white, screen, 360, 529)
        screen.blit(label_image, (125, 50))

        pygame.display.flip()

# функция для отображения окна ргистрации ника
def register_screen():

    #Загрузка переменных и изображений
    nickname = ''
    error_message = ''

    login_image = pygame.image.load("login.png")
    login_image = pygame.transform.scale(login_image, (250, 113))

    screen.fill(black)
    screen.blit(login_image, (260, 90))
    draw_text('(enter your nickname)', pygame.font.Font('freesansbold.ttf', 20), white, screen, 285, 350)
    pygame.draw.rect(screen, white, (250, 300, 300, 30), 2)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Действия клавиатуры и мышки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nickname:
                        error_message = ''
                        write_to_file('user.txt', nickname)
                        rules_screen()
                    else:
                        error_message = 'enter nickname!'
                elif event.key == pygame.K_BACKSPACE:
                    nickname = nickname[:-1]
                else:
                    nickname += event.unicode

        draw_text(nickname, pygame.font.Font('freesansbold.ttf', 25), white, screen, 253, 302)
        draw_text(error_message, pygame.font.Font('freesansbold.ttf', 30), red, screen, 277, 530)

        pygame.display.update()

#функция для вывода правил
def rules_screen():
    screen.fill(black)
    
    with open('user.txt', 'r') as f:
        nickname = f.read()

    restart_button = pygame.Rect(300, 540, 200, 50)
    pygame.draw.rect(screen, black, restart_button)

    #Отображение на экран
    draw_text((str(nickname) + ", Вам придется сразиться с действующим чемпионом мира"), pygame.font.Font('freesansbold.ttf', 20), white, screen, 10, screen_height // 6 - 40)
    draw_text("по пинг-понгу — Фан Чжэндон’ом.",pygame.font.Font('freesansbold.ttf', 20), white, screen, screen_width // 10 - 70, screen_height // 6)
        
    draw_text("Он отбивает все ваши подачи, так что чтобы победить вам нужно отбить",pygame.font.Font('freesansbold.ttf', 20), white, screen, 10, screen_height // 6 + 40)
    draw_text("определенное количество его подач:",pygame.font.Font('freesansbold.ttf', 20), white, screen,  screen_width // 10 - 70, screen_height // 6 + 80)
        
    draw_text("Первый уровень сложности: 10 мячей",pygame.font.Font('freesansbold.ttf', 20), white, screen, 10, screen_height // 6 + 190)
    draw_text("Второй уровень сложности: 20 мячей",pygame.font.Font('freesansbold.ttf', 20), white, screen, 10, screen_height // 6 + 230)
    draw_text("Третий уровень сложности: 30 мячей",pygame.font.Font('freesansbold.ttf', 20), white, screen, 10,  screen_height // 6 + 270)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Действия клавиатуры и мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(mouse_x, mouse_y):
                    levels_screen()

        #Позиция мышки
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if restart_button.collidepoint(mouse_x, mouse_y):
            button_color = green
        else:
            button_color = white

        draw_text('Choose level', pygame.font.Font('freesansbold.ttf', 30), button_color, screen, 320, 550)

        pygame.display.update()


# функция для окна настроек сложности
def levels_screen():

    #Загрузка изображений
    ball_image = pygame.image.load("ball.png")
    ball_image = pygame.transform.scale(ball_image, (250, 250))

    select_image = pygame.image.load("select.png")
    select_image = pygame.transform.scale(select_image, (500, 150))
    select_rect = select_image.get_rect(center=(390, 150))


    button1 = pygame.Rect(50, 300, 200, 50)
    button2 = pygame.Rect(300, 300, 200, 50)
    button3 = pygame.Rect(550, 300, 200, 50)

    screen.fill(black)
    screen.blit(select_image, select_rect.topleft)

    #angle = 0
    #ball_rect = ball_image.get_rect(center=(400, 450))
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Действия клавиатуры и мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button1.collidepoint(mouse_pos):
                    write_to_file('text.txt', 1)
                    game_screen()
                elif button2.collidepoint(mouse_pos):
                    write_to_file('text.txt', 2)
                    game_screen()
                elif button3.collidepoint(mouse_pos):
                    write_to_file('text.txt', 3)
                    game_screen()

        #Позиция мышки
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button1.collidepoint(mouse_x, mouse_y):
            button_color1 = (0, 255, 0)
        else:
            button_color1 = white

        if button2.collidepoint(mouse_x, mouse_y):
            button_color2 = (0, 255, 0)
        else:
            button_color2 = white

        if button3.collidepoint(mouse_x, mouse_y):
            button_color3 = (0, 255, 0)
        else:
            button_color3 = white

        #Отображение на экран
        pygame.draw.rect(screen, button_color1, button1)
        pygame.draw.rect(screen, button_color2, button2)
        pygame.draw.rect(screen, button_color3, button3)

        draw_text('Level 1', pygame.font.Font('freesansbold.ttf', 30), black, screen, 100, 310)
        draw_text('Level 2', pygame.font.Font('freesansbold.ttf', 30), black, screen, 350, 310)
        draw_text('Level 3', pygame.font.Font('freesansbold.ttf', 30), black, screen, 600, 310)
                    
        #rotated_image = pygame.transform.rotate(ball_image, angle)
        #rotated_rect = rotated_image.get_rect(center=ball_rect.center)

        #screen.blit(rotated_image, rotated_rect.topleft)
        #angle += 3

        pygame.display.update()

# функция для главного игрового окна
def game_screen():
    balls = 0
    flag = False
    angle = 0

    #Звгрузка изображений и начальных переменных
    win_image = pygame.image.load("win.png")
    win_image = pygame.transform.scale(win_image, (100, 50))

    background = pygame.image.load('backg.png')
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0, 0))

    player = pygame.image.load("player.png")
    player2 = pygame.image.load("player2.png")

    player_im = player2
    player_rect = player_im.get_rect(center=(400, 250))

    ball_x = random.randint(20, screen_width - 20)
    ball_y = random.randint(20, screen_height // 2 - 20)
    alph = (ball_x - 400) / 100
    bett = ball_y / 70
    ball_radius = 5
    ball_velocity = 3

    sprite_image = pygame.image.load("photo_1.png")
    sprite_rect = sprite_image.get_rect()

    screen.blit(background, (0, 0))
    screen.blit(player_im, player_rect.topleft)
    pygame.display.update()

    for i in range(3, 0, -1):
        screen.blit(background, (0, 0))
        screen.blit(player_im, player_rect.topleft)
        draw_text(str(i), pygame.font.Font('freesansbold.ttf', 70), white, screen, 380, 280)
        time.sleep(1)
        pygame.display.update()

    screen.blit(sprite_image, sprite_rect)
    time.sleep(0.2)
    
    ball_image = pygame.image.load("ball.png")
    ball_image = pygame.transform.scale(ball_image, (ball_radius * 2, ball_radius * 2))

    photo_1 = pygame.image.load("photo_1.png")
    photo_2 = pygame.image.load("photo_2.png")

    with open('text.txt', 'r') as f:
        level = f.read()

    # Main game loop
    running = True
    growing = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Действия клавиатуры и мышки
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused

        if not paused:
            #Физика шарика

            #Обновление координат шарика
            if growing:
                if ball_radius < 20:
                    if ball_radius == 10:
                        player_im = player
                        player_rect = player_im.get_rect(center=(400, 225))
                    ball_y -= ball_velocity
                else:
                    if flag:
                        ball_y += ball_velocity * 1.5
                    else:
                        ball_y += ball_velocity
            else:
                if flag:
                    pik = 33
                else:
                    pik = 20

                if ball_radius < pik:
                    ball_y += ball_velocity * bett
                    ball_x -= 1.5 * alph
                else:
                    ball_y -= ball_velocity * bett
                    ball_x -= 1.5 * alph

            #Обновление радиуса мячика
            if growing:
                if ball_radius < 40:
                    ball_radius += 1
                else:
                    sprite_rect.center = pygame.mouse.get_pos()
                    x = sprite_rect.center[0]
                    y = sprite_rect.center[1]

                    #Проверка столкновения
                    if (abs(x - ball_x) <= (130 + ball_radius)) and (abs(y - ball_y) <= (60 + ball_radius)): #collide
                        balls += 1
                        sprite_image = photo_2

                        player_im = player2
                        player_rect = player_im.get_rect(center=(400, 250))

                        if ball_y < 200:
                            flag = True
                        growing = False
                        
                    else:
                        running = False

            else:
                if ball_y < 280 and ball_radius > 6:
                    ball_radius -= 1 

                    if ball_radius == 25:
                        sprite_image = photo_1

                else:
                    ball_x = random.randint(20, screen_width - 20)
                    ball_y = random.randint(20, screen_height // 2 - 20)
                    alph = (ball_x - 400) / 100
                    bett = ball_y / 70
                    ball_radius = 5
                    flag = False
                    growing = True

            #Позиция мышки
            sprite_rect.center = pygame.mouse.get_pos()

        #Отображение на экран
        screen.blit(background, (0, 0))

        if int(balls) >= int(level) * 10:
            screen.blit(win_image, (80, 25))

        angle = (350 - sprite_rect.x) // 5

        screen.blit(player_im, player_rect.topleft)

        ball_image = pygame.image.load("ball.png")
        ball_image = pygame.transform.scale(ball_image, (ball_radius * 2, ball_radius * 2))

        screen.blit(ball_image, (ball_x, ball_y))
        
        rotated_image = pygame.transform.rotate(sprite_image, angle)
        rotated_rect = rotated_image.get_rect(center=sprite_rect.center)

        screen.blit(rotated_image, rotated_rect.topleft)

        draw_text(str(balls), pygame.font.Font('freesansbold.ttf', 40), white, screen, 30, 40)

        if paused:
            pause_image = pygame.image.load("pause.png")
            screen.blit(pause_image, (300, 200))

        pygame.display.flip()

    final_screen(balls)

# функция для финального окна
def final_screen(balls):
    balls = str(balls)

    with open('text.txt', 'r') as f:
        level = f.read()
    
    with open('user.txt', 'r') as f:
        nickname = f.read()

    my_font = pygame.font.Font('freesansbold.ttf', 30)

    win_label = pygame.image.load('win_label.png')
    win_label = pygame.transform.scale(win_label, (500, 200))

    screen.fill(black)

    if int(balls) < 10:
        x = 330
    else:
        x = 250

    my_text = my_font.render(str(f'{nickname}, вам не хватило до победы: {int(level) * 10 - int(balls)}'), 1, (0, 0, 0))
    text_width = (800 - my_text.get_width()) / 2

    draw_text(f'{balls}', pygame.font.Font('freesansbold.ttf', 250), white, screen, x, 200)
    
    if int(balls) >= int(level) * 10:
        screen.blit(win_label, (130, 20))

    else:
        draw_text(f'{nickname}, вам не хватило до победы: {int(level) * 10 - int(balls)}', pygame.font.Font('freesansbold.ttf', 30), white, screen, text_width, 50)

    restart_button = pygame.Rect(300, 540, 200, 50)
    pygame.draw.rect(screen, black, restart_button)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Действия клавиатуры и мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(mouse_x, mouse_y):
                    levels_screen()

        #Позиция мышки
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if restart_button.collidepoint(mouse_x, mouse_y):
            button_color = green
        else:
            button_color = white

        draw_text('New game', pygame.font.Font('freesansbold.ttf', 30), button_color, screen, 320, 550)

        pygame.display.update()

# запуск основной программы
start_screen()