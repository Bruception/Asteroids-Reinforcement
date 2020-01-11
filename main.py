
import globals as g

import pygame as pg
import sys

from spaceship import SpaceShip
from asteroid import Asteroid

from random import randrange
import math
import heapq

pg.init()

screen = pg.display.set_mode([g.width, g.height])
pg.display.set_caption("Asteroids!")

font = pg.font.Font(None, 30)
clock = pg.time.Clock()

def spawnAsteroid() :
    randomAngle = math.radians(randrange(0, 360))
    randDist = randrange(200, 400)

    ax = 400 + (randDist * math.cos(randomAngle))
    ay = 300 + (randDist * math.sin(randomAngle))

    g.asteroids.append(Asteroid(ax, ay, randomAngle, 60))

for i in range(10) :
    g.ships.append(SpaceShip())

for i in range(8) :
    spawnAsteroid()

deletedShips = []
generation = 0

def update(dt) :

    if(len(g.ships) > 0) :
        for ship in g.ships :
            distances = []
            for asteroid in g.asteroids :
                g.distance(ship, asteroid)
                distances.append(g.distance(ship, asteroid))

            input = heapq.nsmallest(6, distances)
            ship.update(dt, input)

        for bullet in g.bullets :
            bullet.update(dt)
            for asteroid in g.asteroids :
                if(not bullet.delete and g.areColliding(asteroid, bullet)) :
                    asteroid.split()
                    bullet.remove()

        for asteroid in g.asteroids :
            asteroid.update(dt)
            for ship in g.ships :
                if(not ship.delete and g.areColliding(asteroid, ship)) :
                    ship.delete = True
                    deletedShips.append(ship)

        g.bullets = g.filterDelete(g.bullets)
        g.asteroids =  g.filterDelete(g.asteroids)
        g.ships = g.filterDelete(g.ships)

        if(len(g.asteroids) < 8) :
            spawnAsteroid()

    else :
        global generation
        generation += 1

        bestShip = deletedShips[0]
        secondBestShip = deletedShips[1]

        for ship in deletedShips :
            if(ship.fitnessScore > bestShip.fitnessScore) :
                secondBestShip = bestShip
                bestShip = ship
            elif (ship.fitnessScore > secondBestShip.fitnessScore) :
                secondBestShip = ship

        g.bullets.clear()
        g.asteroids.clear()

def draw(screen) :
    screen.fill(g.black)

    for ship in g.ships :
        ship.draw(screen)

    for bullet in g.bullets :
        bullet.draw(screen)

    for asteroid in g.asteroids :
        asteroid.draw(screen)

    if (len(g.ships) > 0) :
        g.ships[0].nn.draw(screen)

    gen = font.render("Generation: " + (str(generation)), True, g.white)

    screen.blit(gen, (600, 20))

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
