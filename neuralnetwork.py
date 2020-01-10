
from io import StringIO
from matrix import Matrix
from random import random
from color import colors
import pygame as pg

def relu(x) :
    return max(0, x)

def rand(x) :
    return random() - random()

class NeuralNetwork :

    def __init__(self, shape) :
        self.weights = []
        self.biases = []
        self.outputs = []
        self.numLayers = len(shape)

        self.x = 100
        self.y = 100
        self.layerMargin = 56
        self.neuronSize = 8
        self.neuronMargin = 18
        self.maxHeight = 0

        for i in range(self.numLayers) :
            r, c = shape[i]
            weights = Matrix(r, c).forEach(rand)
            self.maxHeight = max(self.maxHeight, c)
            self.weights.append(weights)

        self.maxHeight = self.maxHeight * (self.neuronSize + self.neuronMargin)

        for i in range(1, self.numLayers) :
            biases = Matrix(1, self.weights[i].columns).forEach(rand)
            self.biases.append(biases)
            self.outputs.append(None)


    def feedforward(self, input) :
        self.weights[0] = self.weights[0].copyFrom(input)

        output = self.weights[0]

        for i in range(1, self.numLayers) :
            index = i - 1
            self.outputs[index] = output * self.weights[i]
            self.outputs[index] = self.outputs[index] + self.biases[index]
            self.outputs[index] = self.outputs[index].forEach(relu)

        return self.outputs[-1].unpack()

    def __str__(self) :
        outStr = StringIO()

        outStr.write("Weights:\n")

        for w in self.weights :
            outStr.write(str(w))
            outStr.write("\n")

        outStr.write("Biases:\n")

        for b in self.biases :
            outStr.write(str(b))
            outStr.write("\n")

        return outStr.getvalue()

    def draw(self, screen) :
        # Draw neurons
        for i in range(self.numLayers) :
            cols = self.weights[i].columns
            layerHeight = (cols * (self.neuronSize + self.neuronMargin))
            layerOffset = (self.maxHeight / 2) - (layerHeight / 2)

            for c in range(cols) :
                neuronX = self.x + (i * self.layerMargin)
                neuronY = (self.y + layerOffset) + (c * (self.neuronSize + self.neuronMargin))

                pg.draw.circle(screen, colors["white"], [neuronX, int(neuronY)], self.neuronSize)


        # Draw weights
