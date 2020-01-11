from io import StringIO
from random import randrange, random

class Matrix :
    def __init__(self, rows, columns) :
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for j in range(columns)] for i in range(rows)]

    def __mul__(self, other) :
        return self.dot(other)

    def __add__(self, other) :
        return self.add(other)

    def dot(self, other) :
        newMatrix = Matrix(self.rows, other.columns)
        sum = 0

        for i in range(self.rows) :
            for j in range(other.columns) :
                sum = 0
                for k in range(self.columns) :
                    sum = sum + (self.matrix[i][k] * other.matrix[k][j])

                newMatrix.matrix[i][j] = sum

        return newMatrix

    #Element wise addition
    def add(self, other) :
        newMatrix = Matrix(self.rows, self.columns)

        for i in range(self.rows) :
            for j in range(self.columns) :
                newMatrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return newMatrix

    #Apply a function to each element in the matrix
    def forEach(self, func) :
        newMatrix = Matrix(self.rows, self.columns)

        for i in range(self.rows) :
            for j in range(self.columns) :
                newMatrix.matrix[i][j] = func(self.matrix[i][j])

        return newMatrix

    #Copy contents from a 2D array
    def copyFrom(self, m) :
        newMatrix = Matrix(self.rows, self.columns)

        for i in range(self.rows) :
            for j in range(self.columns) :
                newMatrix.matrix[i][j] = m[i][j]

        return newMatrix

    def unpack(self) :
        unpacked = []

        for i in range(self.rows) :
            for j in range(self.columns) :
                unpacked.append(self.matrix[i][j])

        return unpacked


    #(i < randR) or (i == randR and j <= randC)

    def crossover(self, other) :
        newMatrix = Matrix(self.rows, self.columns)

        randRow = randrange(0, self.rows - 1)
        randCol = randrange(0, self.cols - 1)

        for i in range(self.rows) :
            for j in range(self.columns) :
                if(i <= randRow or j <= randCol) :
                    newMatrix.matrix[i][j] = self.matrix[i][j]
                else :
                    newMatrix.matrix[i][j] = other.matrix[i][j]

                if(random() <= 0.05) :
                    newMatrix.matrix[i][j] = random() - random()


        return newMatrix

    def __str__(self) :
        outStr = StringIO()

        for i in range(self.rows) :
            for j in range(self.columns) :
                outStr.write(str(self.matrix[i][j]))
                outStr.write("\t")
            outStr.write("\n")

        return outStr.getvalue()
