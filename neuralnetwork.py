import pygame as pg
import globals as g

from io import StringIO
from matrix import Matrix
from random import random

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

        self.x = 20
        self.y = 20
        self.layerMargin = 36
        self.neuronSize = 4
        self.neuronMargin = 6
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

        self.neuronCoords = []
        self.computeNeuronCoords()

    def feedforward(self, input) :
        self.weights[0] = self.weights[0].copyFrom(input)

        output = self.weights[0]

        for i in range(1, self.numLayers) :
            index = i - 1
            self.outputs[index] = output * self.weights[i]
            self.outputs[index] = self.outputs[index] + self.biases[index]
            self.outputs[index] = self.outputs[index].forEach(relu)
            output = self.outputs[index]

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

    def computeNeuronCoords(self) :
        for i in range(self.numLayers) :
            cols = self.weights[i].columns
            layerHeight = (cols * (self.neuronSize + self.neuronMargin))
            layerOffset = (self.maxHeight / 2) - (layerHeight / 2)
            self.neuronCoords.append([])
            for c in range(cols) :
                neuronX = self.x + (i * self.layerMargin)
                neuronY = (self.y + layerOffset) + (c * (self.neuronSize + self.neuronMargin))
                self.neuronCoords[i].append([int(neuronX), int(neuronY)])

    def draw(self, screen) :
        if(self.outputs[0] == None) :
            return
        # Draw Network
        color = None
        for i in range(self.numLayers) :
            for n in range(self.weights[i].columns) :
                neuron = self.neuronCoords[i][n]
                if(i < self.numLayers - 1) :
                    for n2 in range(self.weights[i + 1].columns) :
                        neuron2 = self.neuronCoords[i + 1][n2]

                        weight = self.weights[i + 1].matrix[n][n2]
                        color = (weight >= 0) and g.blue or g.red
                        weight = int(abs(weight * 6))
                        weight = weight > 0 and weight or 1

                        pg.draw.line(screen, color, neuron, neuron2, weight)

                out = (i == 0) and 1 or self.outputs[i - 1].matrix[0][n]
                color = (out > 0) and g.white or g.black_dark

                pg.draw.circle(screen, color, self.neuronCoords[i][n], self.neuronSize)