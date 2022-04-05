class DisjointSet:
    def __init__(self, length):
        self.unionDict = {}

        for vertice in range (length):
            self.unionDict[vertice] = -1
        
    def isJoint(self, vertice1, vertice2):
        parent1 = self.find(vertice1)
        parent2 = self.find(vertice2)

        if parent1 == parent2:
            return True
        return False
    
    def find(self, vertice):
        curr = vertice

        while self.unionDict[curr] > 0:
            curr = self.unionDict[curr]

        return curr      
        
    def union(self, vertice1, vertice2):        
        if self.isJoint(vertice1, vertice2):
            return

        parent1 = self.find(vertice1)
        parent2 = self.find(vertice2)
        
        size1 = abs(self.unionDict[parent1])
        size2 = abs(self.unionDict[parent2])

        if size1 < size2:
            self.unionDict[parent1] = parent2
            self.unionDict[parent2] = -(size1 + size2)
        else:
            self.unionDict[parent2] = parent1
            self.unionDict[parent1] = -(size1 + size2)
