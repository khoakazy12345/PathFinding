import PathFinding
import SampleGraph

sampleGraph1 = SampleGraph.RandomGraph(4)
sampleGraph1.addEdge(0,1,400)
sampleGraph1.addEdge(1,2,400)
sampleGraph1.addEdge(2,3,1)
sampleGraph1.addEdge(3,0,2000)

PathFinding.findPath(sampleGraph1.getGraph(), 2, 0)

