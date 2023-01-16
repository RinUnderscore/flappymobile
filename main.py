import pygame as pg
from pygame.locals import *
import time
import random

screensize = (440,760)

score = 0

player_x = 80-25
player_y = 380-25
player_data = (player_x, player_y, 50, 50)
player_y_change = 0
player_y_accel = 0

randomizer_a = random.randint(-150,150)
pipe_a_x = 300
pipe_a_y = -500 + randomizer_a

randomizer_b = random.randint(-150,150)
pipe_b_x = 600
pipe_b_y = -500 + randomizer_b

randomizer_c = random.randint(-150,150)
pipe_c_x = 900
pipe_c_y = -500 + randomizer_c

a_pass = False
b_pass = False
c_pass = False

pg.init()
screen = pg.display.set_mode(screensize)
pg.display.set_caption("FlappyMobile Clone")
run = True

while run:

    screen.fill((255,255,255))
    pg.draw.rect(screen,(0,0,0), pg.Rect(player_data))

    time.sleep(0.01)
    if player_y_accel > 8:
        player_y_accel = 8
    elif player_y_accel < 8:
        player_y_accel += 0.1
    
    player_y_change += player_y_accel

    player_data = (player_x, player_y + player_y_change, 50, 50)

    # Pipe Code
    pg.draw.rect(screen,(0,0,0), pg.Rect((pipe_a_x,pipe_a_y,80,700)))
    pg.draw.rect(screen,(0,0,0), pg.Rect((pipe_a_x,pipe_a_y + 900, 80,700)))
    
    pipe_a_x -= 3

    # Pipe 2 Code
    pg.draw.rect(screen,(0,0,0), pg.Rect((pipe_b_x,pipe_b_y,80,700)))
    pg.draw.rect(screen,(0,0,0), pg.Rect((pipe_b_x,pipe_b_y + 900, 80,700)))
    
    pipe_b_x -= 3

    # Pipe 3 Code
    pg.draw.rect(screen,(0,0,0), pg.Rect((pipe_c_x,pipe_c_y,80,700)))
    pg.draw.rect(screen,(0,0,0), pg.Rect((pipe_c_x,pipe_c_y + 900, 80,700)))
    
    pipe_c_x -= 3

    # Check for Passed Pipe
    if pipe_a_x < 80-25 and a_pass == False and not pipe_a_x < (80-25-60):
        score += 1
        a_pass = True
    if pipe_b_x < 80-25 and b_pass == False and not pipe_b_x < (80-25-60):
        score += 1
        b_pass = True
    if pipe_c_x < 80-25 and c_pass == False and not pipe_c_x < (80-25-60):
        score += 1
        c_pass = True

    if a_pass == True and pipe_a_x < (80-25-60):
        a_pass = False
    if b_pass == True and pipe_b_x < (80-25-60):
        b_pass = False
    if c_pass == True and pipe_c_x < (80-25-60):
        c_pass = False

    print(score)


    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player_y_change -= 60
                player_y_accel = 0
        if event.type == pg.QUIT:
            run = False