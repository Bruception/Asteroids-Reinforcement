import pygame as pg
import math

import globals as g

class Bullet :
    def __init__(self, x, y, angle) :
        self.x = x
        self.y = y

        self.angle = angle
        self.vel = 550

        self.width = 3
        self.height = 3

        self.radius = 3

        self.delete = False

        self.vx = math.cos(self.angle) * self.vel
        self.vy = math.sin(self.angle) * self.vel

    def bound(self) :
        boundX = (self.x - self.radius <= 0) or (self.x + self.radius >= 800)
        boundY = (self.y - self.radius <= 0) or (self.y + self.radius >= 600)

        self.delete = boundX or boundY

    def update(self, dt) :
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.bound()

    def draw(self, screen) :
        pg.draw.circle(screen, g.white, [int(self.x), int(self.y)], self.radius)