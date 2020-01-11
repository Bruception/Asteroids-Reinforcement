import pygame as pg

import globals as g

from bullet import Bullet
from neuralnetwork import NeuralNetwork
from matrix import Matrix

import math
from random import random

shape = [(1, 6), (6, 12), (12, 12), (12, 12), (12, 12), (12, 4)]

pointOffsets = [
    [15, 0],
    [-15, -15],
    [-7, 0],
    [-15, 15]
]

def rotate(origin, points, angle) :
    ox, oy = origin[0], origin[1]

    sin = math.sin
    cos = math.cos

    for point in points :
        dx = point[0] - ox
        dy = point[1] - oy

        rx = dx * cos(angle) - dy * sin(angle)
        ry = dx * sin(angle) + dy * cos(angle)

        point[0] = rx + ox
        point[1] = ry + oy

class SpaceShip :

    def __init__(self) :
        self.x = 400
        self.y = 300
        self.radius = 15

        self.shootTimer = 0

        self.points = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]
        ]

        self.vel = 100
        self.angle = 0
        self.nn = NeuralNetwork(shape)

        self.delete = False

    def update(self, dt, input) :
        self.computeActions(dt, input)
        g.bound(self)
        self.computePoints()

    def computeActions(self, dt, input) :
        output = self.nn.feedforward([input])

        if(output[0] > 0) :
            self.angle += 4 * dt
        if(output[1] > 0) :
            self.angle -= 4 * dt

        self.vel = (self.vel + 300 * dt) if(output[2] > 0) else self.vel
        self.vel = min(self.vel, 800)

        self.x += self.vel * math.cos(self.angle) * dt
        self.y += self.vel * math.sin(self.angle) * dt

        self.vel *= 0.98

        if(output[3] > 0) :
            self.shootTimer += dt

            if(self.shootTimer >= 0.25) :
                g.bullets.append(Bullet(self.x, self.y, self.angle))
                self.shootTimer = 0

    def computePoints(self) :
        for i in range(4) :
            point = self.points[i]

            point[0] = self.x + pointOffsets[i][0]
            point[1] = self.y + pointOffsets[i][1]

        rotate([self.x, self.y], self.points, self.angle)

    def draw(self, screen) :
        pg.draw.polygon(screen, g.white, self.points, 4)
        #pg.draw.circle(screen, g.white, [int(self.x), int(self.y)], self.radius, 2)
