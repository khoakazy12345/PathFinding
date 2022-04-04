import DisjointSet
import heapq
from collections import defaultdict

graph1 = [[-1, 400, -1, 2000],[400, -1, 400, -1],[-1, 400, -1, 1], [2000, -1, 1, -1]]

def edgeGenerate(graph):
    edgeDict = defaultdict(list)

    for vertice in range (len(graph)):
        for neighbor in range (len(graph[vertice])):
            if graph[vertice][neighbor] == -1:
                continue
            edgeDict[vertice].append(neighbor)

    return edgeDict

def weightGenerate(graph):
    weightDict = defaultdict(int)

    for vertice in range (len(graph)):
        for neighbor in range (vertice, len(graph[vertice])):
            if graph[vertice][neighbor] == -1:
                continue
            weightDict[(vertice, neighbor)] = graph[vertice][neighbor]
    
    return weightDict

def findPath(graph, start, end):
    ds = DisjointSet(len(graph))
    edgeDict = edgeGenerate(graph)
    weightDict = weightGenerate(graph)  
    edgeHeap = []

    

    return
