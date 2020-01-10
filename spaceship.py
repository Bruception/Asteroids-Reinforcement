
import pygame as py
from color import colors
from neuralnetwork import NeuralNetwork
from random import random
import math

white = colors["white"]
shape = [(1, 3), (3, 11), (11, 11), (11, 11), (11, 11), (11, 4)]

class SpaceShip :

    def __init__(self) :
        self.x = 375
        self.y = 275
        self.width = 30
        self.height = 30
        self.vel = 100
        self.angle = math.pi
        self.nn = NeuralNetwork(shape)

    def bound(self) :
        self.x = self.x if(self.x + self.width < 800) else 800 - self.width
        self.x = 0 if(self.x <= 0) else self.x
        self.y = self.y if (self.y + self.height < 600) else 600 - self.height
        self.y = 0 if(self.y <= 0) else self.y

    def update(self, dt) :

        output = self.nn.feedforward([[10 * random(), 10 * random(), 10 * random()]])

        self.angle = self.angle + output[0] * dt
        self.angle = self.angle - output[1] * dt
        self.vel = min(100 * output[2], 200)

        self.x += self.vel * math.cos(self.angle) * dt
        self.y += self.vel * math.sin(self.angle) * dt

        self.bound()

    def draw(self, screen) :
        py.draw.rect(screen, white, [self.x, self.y, self.width, self.height])

        angleX = (self.x + self.width * 0.5) + 60 * math.cos(self.angle)
        angleY = (self.y + self.height * 0.5) + 60 * math.sin(self.angle)

        py.draw.line(screen, white, [self.x + self.width * 0.5, self.y + self.height * 0.5], [angleX, angleY])

        self.nn.draw(screen)