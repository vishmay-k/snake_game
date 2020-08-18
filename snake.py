#importing and initialising
import pygame
pygame.init()

#game variables needed for game window
screen_width = 800
screen_height = 400

#creating game window and seting up the name of the game and updating window display
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake")
pygame.display.update()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
vel_x = 10
vel_y = 0
fps = 30

clock = pygame.time.Clock()

#game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x = 10
                vel_y = 0
            if event.key == pygame.K_LEFT:
                vel_x = - 10
                vel_y = 0
            if event.key == pygame.K_DOWN:
                vel_y = 10
                vel_x = 0
            if event.key == pygame.K_UP:
                vel_y = - 10
                vel_x = 0

    snake_x = snake_x + vel_x
    snake_y = snake_y + vel_y

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,[snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
