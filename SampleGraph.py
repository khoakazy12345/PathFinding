class RandomGraph:
    def __init__(self, length):
        self.matrix = [[-1 for i in range (length)] for i in range (length)]
        self.length = length
    
    def addEdge(self, vertice1, vertice2, weight = 0):
        if vertice1 > self.length or vertice2 > self.length:
            print('Vertice limit exceeded. Pick a smaller number.')
            return
        
        if vertice1 == vertice2:
            print("Two vertices have to be different")
            return
        
        self.matrix[vertice1][vertice2] = weight
        self.matrix[vertice2][vertice1] = weight
    
    def getGraph(self):
        return self.matrix