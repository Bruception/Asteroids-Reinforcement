
import globals as g

import pygame as pg
import sys
from spaceship import SpaceShip
from asteroid import Asteroid

myAsteroid = Asteroid(400, 300, 1, False)

pg.init()

screen = pg.display.set_mode([g.width, g.height])
pg.display.set_caption("Asteroids!")

font = pg.font.Font(None, 30)
clock = pg.time.Clock()

for i in range(5) :
    g.ships.append(SpaceShip())

def update(dt) :

    myAsteroid.update(dt)

    for ship in g.ships :
        ship.update(dt)

        if(g.areColliding(ship, myAsteroid)) :
            print("Collision! with", ship)

    for bullet in g.bullets :
        bullet.update(dt)

    g.bullets = list(filter(lambda b : not b.delete, g.bullets))

def draw(screen) :
    screen.fill(g.black)

    for ship in g.ships :
        ship.draw(screen)

    for bullet in g.bullets :
        bullet.draw(screen)

    g.ships[0].nn.draw(screen)

    myAsteroid.draw(screen)

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
