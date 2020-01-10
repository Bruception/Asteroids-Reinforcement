
import pygame as py
from color import colors
from neuralnetwork import NeuralNetwork

white = colors["white"]

class SpaceShip :

    def __init__(self) :
        self.posAndDim = [400, 300, 30, 30]

    def draw(self, screen) :
        py.draw.rect(screen, white, self.posAndDim)