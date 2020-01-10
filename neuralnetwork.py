
from cStringIO import StringIO
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

        numLayers = len(shape)

        for i in range(numLayers) :
            r, c = shape[i]
            weights = Matrix(r, c).forEach(rand)
            self.weights.append(weights)

        for i in range(1, numLayers) :
            biases = Matrix(1, self.weights[i].columns).forEach(rand)
            self.biases.append(biases)


    def feedforward(self) :
        print("Feeding forward!")

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


nn = NeuralNetwork([(1, 3), (3, 3), (3, 3), (3, 4), (4, 2)])
print(nn)