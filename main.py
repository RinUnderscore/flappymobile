import pygame as pg
from pygame.locals import *
import time
import os
import sys

screensize = (440,760)

player_x = 80-25
player_y = 380-25
player_data = (player_x, player_y, 50, 50)

pg.init()
screen = pg.display.set_mode(screensize)
pg.display.set_caption("FlappyMobile Clone")
run = True

while run:

    screen.fill((255,255,255))
    pg.draw.rect(screen,(0,0,0), pg.Rect(player_data))


    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player_y -= 50
                player_data = (player_x, player_y, 50, 50)
        if event.type == pg.QUIT:
            run = False