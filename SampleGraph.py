import random

class RandomGraph:
    def __init__(self, length):
        self.matrix = [[-1 for i in range (length)] for i in range (length)]
        self.verticeCount = length
        self.edgeCount = 0
    
    def addEdge(self, vertice1, vertice2, weight = 0):
        if vertice1 > self.verticeCount or vertice2 > self.verticeCount:
            print('Vertice limit exceeded. Pick a smaller number.')
            return
        
        if vertice1 == vertice2:
            print("Two vertices have to be different")
            return
        
        self.edgeCount += 1
        self.matrix[vertice1][vertice2] = weight
        self.matrix[vertice2][vertice1] = weight
    
    def getGraph(self):
        return self.matrix

    def generateGraph(self, probability, minWeight, maxWeight):
        for i in range (0, self.verticeCount - 1):
            for j in range (i + 1, self.verticeCount):
                if random.random() <= probability:
                    self.addEdge(i , j, random.randint(minWeight, maxWeight))
    
