
import pygame as pg
from color import colors

pg.init()
font = pg.font.Font(None, 30)
clock = pg.time.Clock()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("Asteroids!")

running = True

while (running) :
    for event in pg.event.get() :
        if (event.type == pg.QUIT) :
            running = False

    screen.fill(colors["black"])
    fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
    screen.blit(fps, (750, 30))
    clock.tick(30)

    pg.display.flip()

pg.quit()