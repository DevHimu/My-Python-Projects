#Steps to create to Snake Game

#1. Create the Screen
#2. Create the Snake
#3. Move the Snake
#4. Creating Game Over and Boundaries

import pygame
import time
import random
pygame.init()

#1. Create the Screen
screen =  pygame.display.set_mode((800, 800))
pygame.display.update()
pygame.display.set_caption("SNAKE GAME")

#RGB = RED GREEN BLUE

#color variables
red = (255,0,0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0,0,0)
yellow = (100,100,0)

#screen_variables
screen_width = 600
screen_height = 800

# x and y Coordinates
x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 0

font_style = pygame.font.SysFont(None, 50)

#Game Over Message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/2, screen_height/2])

game_over = False

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #3. Move the Snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10


    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    screen.fill(black)
    
    clock.tick(30)

    #2. Snake Creation
    pygame.draw.rect(screen, yellow, [x1,y1,20,20])
    pygame.display.update()

    clock.tick(snake_speed)

message("Game Over", red)
pygame.display.update()
time.sleep(2)

        
pygame.quit()
quit()
