
import globals as g

import pygame as pg
import sys
from spaceship import SpaceShip

pg.init()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("Asteroids!")

font = pg.font.Font(None, 30)
clock = pg.time.Clock()

mySpace = SpaceShip()

def update(dt) :
    mySpace.update(dt)

    for bullet in g.bullets :
        bullet.update(dt)

    g.bullets = list(filter(lambda b : not b.delete, g.bullets))

def draw(screen) :
    screen.fill(g.black)

    mySpace.draw(screen)

    for bullet in g.bullets :
        bullet.draw(screen)

    fps = font.render(str(int(clock.get_fps())), True, g.white)
    screen.blit(fps, (750, 30))

def main() :
    running = True
    while (running) :
        for event in pg.event.get() :
            if (event.type == pg.QUIT) :
                running = False

        dt = 1 / (clock.tick(30))

        update(dt)
        draw(screen)

        pg.display.flip()

    pg.quit()
    sys.exit()

main()