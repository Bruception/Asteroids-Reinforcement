
import pygame as pg
from color import colors
from neuralnetwork import NeuralNetwork
from random import random
from matrix import Matrix
import math

white = colors["white"]
shape = [(1, 3), (3, 11), (11, 11), (11, 11), (11, 11), (11, 4)]


def rotate(origin, points, angle) :
    ox, oy = origin[0], origin[1]

    for point in points :
        dx = point[0] - ox
        dy = point[1] - oy

        rx = dx * math.cos(angle) - dy * math.sin(angle)
        ry = dx * math.sin(angle) + dy * math.cos(angle)

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
        self.determineActions(dt)
        self.bound()
        self.computePoints()

    def determineActions(self, dt) :
        output = self.nn.feedforward([[10 * random(), 10 * random(), 10 * random()]])

        self.angle = self.angle + output[0] * dt
        self.angle = self.angle - output[1] * dt
        self.vel = min(100 * output[2], 200)

        self.x += self.vel * math.cos(self.angle) * dt
        self.y += self.vel * math.sin(self.angle) * dt

    def bound(self) :
        self.x = self.x if(self.x + self.width < 800) else 800 - self.width
        self.x = 0 if(self.x <= 0) else self.x
        self.y = self.y if (self.y + self.height < 600) else 600 - self.height
        self.y = 0 if(self.y <= 0) else self.y

    def computePoints(self) :
        self.centerX = self.x + self.width * 0.5
        self.centerY = self.y + self.height * 0.5

        self.points[0][0], self.points[0][1] = self.centerX + 15, self.centerY
        self.points[1][0], self.points[1][1] = self.centerX - 15, self.centerY - 15
        self.points[2][0], self.points[2][1] = self.centerX - 7, self.centerY
        self.points[3][0], self.points[3][1] = self.centerX - 15, self.centerY + 15

    def draw(self, screen) :

        rotate([self.centerX, self.centerY], self.points, self.angle)
        pg.draw.polygon(screen, white, self.points, 2)

        self.nn.draw(screen)
