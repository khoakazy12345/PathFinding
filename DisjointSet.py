class DisjointSet:
    def __init__(self, vertices):
        self.unionDict = {}

        for vertice in vertices:
            self.unionDict[vertice] = -1
    
    def find(self, vertice):
        curr = vertice

        while self.unionDict[curr] > 0:
            curr = self.unionDict[curr]

        return curr      
        
    def union(self, vertice1, vertice2):        
        parent1 = self.find(vertice1)
        parent2 = self.find(vertice2)

        if parent1 == parent2:
            print("These are in the same set")
            return
        
        size1 = abs(self.unionDict[parent1])
        size2 = abs(self.unionDict[parent2])

        if size1 < size2:
            self.unionDict[parent1] = parent2
            self.unionDict[parent2] = -(size1 + size2)
        else:
            self.unionDict[parent2] = parent1
            self.unionDict[parent1] = -(size1 + size2)

ds = DisjointSet([1,2,3,4,5,6,7,8])
print(ds.unionDict)
ds.union(1,2)
print(ds.unionDict)
ds.union(3,4)
print(ds.unionDict)
ds.union(5,6)
print(ds.unionDict)
ds.union(7,8)
print(ds.unionDict)
ds.union(2,4)
print(ds.unionDict)
ds.union(2,5)
print(ds.unionDict)
ds.union(5,7)
print(ds.unionDict)
