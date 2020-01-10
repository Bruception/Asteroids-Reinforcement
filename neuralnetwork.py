
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

        for i in range(self.numLayers) :
            r, c = shape[i]
            weights = Matrix(r, c).forEach(rand)
            self.weights.append(weights)

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


# Turn Left, Turn Right, Move up, Shoot
nn = NeuralNetwork([(1, 3), (3, 3), (3, 3), (3, 4)])
print(nn.feedforward([[1, 2, 3]]))
