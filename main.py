
import pygame as pg
import color

colors = color.colors

pg.init()

screen = pg.display.set_mode([800, 600])

running = True

while (running) :
    for event in pg.event.get() :
        if (event.type == pg.QUIT) :
            running = False

    screen.fill(colors["black"])
    pg.draw.rect(screen, colors["red"], [0, 0, 200, 200])
    pg.display.update()

pg.quit()