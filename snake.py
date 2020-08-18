#importing and initialising
import pygame
import random
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
snake_x = screen_width/2
snake_y = screen_height/2
snake_size = 10
eat_size = 0.75*snake_size
food_x = random.randint(50,screen_width-50)
food_y = random.randint(50,screen_height-50)
init_vel = 3
vel_x = init_vel
vel_y = 0
fps = 60
score = 0

font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

def screen_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

#game loop
while not exit_game:
    for event in pygame.event.get():
        #print(event)
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

    snake_x = snake_x + vel_x
    snake_y = snake_y + vel_y
    if abs(snake_x-food_x) < eat_size and abs(snake_y-food_y) < eat_size:
        score += 1
        food_x = random.randint(50, screen_width / 2)
        food_y = random.randint(50, screen_height / 2)
    gamewindow.fill(white)
    screen_score("SCORE :" + str(score * 10), blue, 5, 5)
    pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gamewindow,black,[snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
