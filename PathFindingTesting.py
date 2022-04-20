import PathFinding
import SampleGraph
from datetime import datetime
import random

# sampleGraph1 = SampleGraph.RandomGraph(4)
# sampleGraph1.addEdge(0,1,400)
# sampleGraph1.addEdge(1,2,400)
# sampleGraph1.addEdge(2,3,1)
# sampleGraph1.addEdge(3,0,2000)

# PathFinding.findPath(sampleGraph1.getGraph(), 2, 0)


# sampleGraph2 = SampleGraph.RandomGraph(8)
# sampleGraph2.addEdge(0,3,220)
# sampleGraph2.addEdge(0,7,121)
# sampleGraph2.addEdge(0,2,207)
# sampleGraph2.addEdge(0,5,311)
# sampleGraph2.addEdge(1,7,550)
# sampleGraph2.addEdge(1,6,30)
# sampleGraph2.addEdge(2,7,337)
# sampleGraph2.addEdge(2,5,159)
# sampleGraph2.addEdge(2,6,40)
# sampleGraph2.addEdge(3,4,700)
# sampleGraph2.addEdge(4,7,100)

# PathFinding.findPath(sampleGraph2.getGraph(), 4, 6)
for i in range (5):
    initTime = datetime.now()
    size = 500

    sampleGraph3 = SampleGraph.RandomGraph(size)
    sampleGraph3.generateGraph(0.5, 100, 400)
    generateTime = datetime.now()

    start = random.randint(0, size - 1)
    end = random.randint(0, size - 1)
    result = PathFinding.findPath(sampleGraph3.getGraph(), start, end)
    excutionTime = datetime.now()

    print((generateTime - initTime).microseconds)
    print((excutionTime - generateTime).microseconds)

