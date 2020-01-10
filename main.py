
import pygame as pg

pg.init()

screen = pg.display.set_mode([800, 600])

running = True

while (running) :
    for event in pg.event.get() :
        if (event.type == pg.QUIT) :
            running = False


pg.quit()