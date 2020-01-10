
import pygame as pg
import color

pg.init()

screen = pg.display.set_mode([800, 600])

running = True

while (running) :
    for event in pg.event.get() :
        if (event.type == pg.QUIT) :
            running = False

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 0, 0), [0, 0, 200, 200])
    pg.display.update()

pg.quit()