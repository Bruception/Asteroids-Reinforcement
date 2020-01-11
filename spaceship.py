import pygame as pg

import globals as g

from bullet import Bullet
from neuralnetwork import NeuralNetwork
from matrix import Matrix

import math
from random import random

shape = [(1, 3), (3, 11), (11, 11), (11, 11), (11, 11), (11, 4)]

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
        self.x = 375
        self.y = 275
        self.width = 30
        self.height = 30

        self.centerX = self.x + self.width * 0.5
        self.centerY = self.y + self.height * 0.5

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

    def update(self, dt) :
        self.computeActions(dt)
        self.bound()
        self.computePoints()

    def computeActions(self, dt) :
        output = self.nn.feedforward(
            [[10 * random(), 10 * random(), 10 * random()]]
        )

        self.angle += output[0] * dt
        self.angle -= output[1] * dt
        self.vel = min(100 * output[2], 200)

        self.x += self.vel * math.cos(self.angle) * dt
        self.y += self.vel * math.sin(self.angle) * dt

        self.centerX = self.x + self.width * 0.5
        self.centerY = self.y + self.height * 0.5

        if(output[3] > 0) :
            self.shootTimer += dt

            if(self.shootTimer >= 0.25) :
                g.bullets.append(Bullet(self.centerX, self.centerY, self.angle))
                self.shootTimer = 0

    def bound(self) :
        self.x = self.x if(self.x + self.width <= 800) else 800 - self.width
        self.x = 0 if(self.x <= 0) else self.x
        self.y = self.y if (self.y + self.height <= 600) else 600 - self.height
        self.y = 0 if(self.y <= 0) else self.y

    def computePoints(self) :
        for i in range(4) :
            point = self.points[i]

            point[0] = self.centerX + pointOffsets[i][0]
            point[1] = self.centerY + pointOffsets[i][1]

        rotate([self.centerX, self.centerY], self.points, self.angle)

    def draw(self, screen) :
        pg.draw.polygon(screen, g.white, self.points, 2)
        self.nn.draw(screen)
