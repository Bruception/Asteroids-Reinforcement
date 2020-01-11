
import pygame as pg
import globals as g

import math
from random import random

class Asteroid :

    def __init__(self, x, y, angle, radius) :
        self.x = x
        self.y = y
        self.angle = angle

        self.vel = 200

        self.vx = math.cos(self.angle) * self.vel
        self.vy = math.sin(self.angle) * self.vel

        self.radius = radius

        self.delete = False

        self.points = []
        self.offsets = []

        for i in range(0, 360, 30) :

            offsetX = self.radius + (-random()) * (self.radius / 3)
            offsetY = self.radius + (-random()) * (self.radius / 3)

            offsetX *= math.cos(math.radians(i))
            offsetY *= math.sin(math.radians(i))

            pointX = self.x + offsetX
            pointY = self.y + offsetY

            point = [pointX, pointY]
            offset = [offsetX, offsetY]

            self.points.append(point)
            self.offsets.append(offset)

    def update(self, dt) :
        self.x += self.vx * dt
        self.y += self.vy * dt

        g.bound(self)
        self.computeCoords()

    def split(self) :
        self.delete = True

        halfRadius = int(self.radius / 2)

        if(halfRadius > 10) :
            g.asteroids.append(Asteroid(self.x, self.y, random(), halfRadius))
            g.asteroids.append(Asteroid(self.x, self.y, random(), halfRadius))

    def computeCoords(self) :
        for i in range(len(self.points)) :
            self.points[i][0] = self.x + self.offsets[i][0]
            self.points[i][1] = self.y + self.offsets[i][1]

    def draw(self, screen) :
        pg.draw.polygon(screen, g.red, self.points, 2)
        #pg.draw.circle(screen, g.white, [int(self.x), int(self.y)], self.radius, 2)
