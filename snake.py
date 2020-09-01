# importing and initialising
import pygame
import random
pygame.init()

# game variables needed for game window
screen_width = 800
screen_height = 400

# creating game window and seting up the name of the game and updating window display
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake")
pygame.display.update()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# setting font for text on screen
font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()


# function which shows score on screen
def screen_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


# fuction which plots snake on the game window
def plot_snake(gamewin, color, snk_list, size):
    for x, y in snk_list:
        pygame.draw.rect(gamewin, color, [x, y, size, size])


def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(green)
        screen_score("WELCOME TO SNAKE", black, screen_width * 0.33, screen_height * 0.40)
        screen_score("PRESS SPACEBAR TO PLAY", black, screen_width * 0.28, screen_height * 0.50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloopin()
        pygame.display.update()
        clock.tick(60)


# game loop
def gameloopin():
    # list used to make snake grow
    snake_list = []
    snake_length = 1
    # game specific variables which needs to be updated in game loop
    exit_game = False
    game_over = False
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_size = 10
    eat_size = 0.75 * snake_size
    food_x = random.randint(50, screen_width - 50)
    food_y = random.randint(50, screen_height - 50)
    init_vel = 3
    vel_x = init_vel
    vel_y = 0
    fps = 60
    score = 0

    # high score file open
    with open("hscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            gamewindow.fill(black)
            screen_score("  SNAKE", green, screen_width * 0.42, 10)
            screen_score("GAME OVER !", green, screen_width * 0.40, screen_height * 0.25)
            screen_score(f"SCORE : {score}", green, screen_width * 0.41, screen_height * 0.36)
            screen_score(f"HIGH SCORE : {hiscore}", green, screen_width * 0.36, screen_height * 0.46)
            screen_score("PRESS SPACEBAR TO CONTINUE", green, screen_width * 0.25, screen_height * 0.58)
            # high score file open to write
            with open("hscore.txt", "w") as f:
                f.write(str(hiscore))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome()
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = init_vel
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x = - init_vel
                        vel_y = 0
                    if event.key == pygame.K_DOWN:
                        vel_y = init_vel
                        vel_x = 0
                    if event.key == pygame.K_UP:
                        vel_y = - init_vel
                        vel_x = 0
                    if event.key == pygame.K_q:
                        score += 10
                    if event.key == pygame.K_0:
                        exit_game = True

            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y
            if abs(snake_x-food_x) < eat_size and abs(snake_y-food_y) < eat_size:
                score += 10
                food_x = random.randint(50, screen_width / 2)
                food_y = random.randint(50, screen_height / 2)
                snake_length += 5
                if score > int(hiscore):
                    hiscore = score

            gamewindow.fill(white)
            screen_score("  SNAKE    SCORE :" + str(score) + "    HIGH SCORE: " + str(hiscore) + "        0 - EXIT", black, 5, 5)
            pygame.draw.rect(gamewindow, green, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 35 or snake_y > screen_height:
                game_over = True

            plot_snake(gamewindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
