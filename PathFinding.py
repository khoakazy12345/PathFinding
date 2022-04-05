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
        for neighbor in range (len(graph[vertice])):
            if graph[vertice][neighbor] == -1:
                continue
            weightDict[(vertice, neighbor)] = graph[vertice][neighbor]
    
    return weightDict

def findPath(graph, start, end):
    ds = DisjointSet.DisjointSet(len(graph))
    edgeDict = edgeGenerate(graph)
    weightDict = weightGenerate(graph)  
    visitedNodes = {end: -1}
    edgeHeap = []

    for neighbor in edgeDict[end]:
        weight = weightDict[(end, neighbor)]
        heapq.heappush(edgeHeap, [-weight, end, neighbor])
    
    while start not in visitedNodes and edgeHeap:
        weight, fromNode, toNode = heapq.heappop(edgeHeap)

        if ds.isJoint(end, toNode):
            continue
        
        visitedNodes[toNode] = fromNode
        ds.union(end, toNode)

        for neighbor in edgeDict[toNode]:
            if neighbor not in visitedNodes:
                weight = weightDict[(toNode, neighbor)]
                heapq.heappush(edgeHeap, [-weight, toNode, neighbor])

    print(visitedNodes)
    return visitedNodes
