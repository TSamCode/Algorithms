class Node():
    
    def __init__(self, data):
        self.data = data
        self.neighbours = {}

    def __str__(self):
        return str(self.data) + ' has adjacent nodes: ' + str([node.data for node in self.neighbours])
    
    def addNeighbour(self, theNeighbour, weight = 0):
        self.neighbours[theNeighbour] = weight

    def getNeighbours(self):
        return self.neighbours.keys()

    def getNode(self):
        return self.data

    def getWeights(self, theNeighbour):
        return self.neighbours[theNeighbour]    

class Graph():
    
    def __init__(self):
        self.numNodes = 0
        self.nodes = {}

    def __iter__(self):
        return iter(self.nodes.values())

    def addNode(self, theNode):
        self.numNodes += 1
        self.nodes[theNode] = Node(theNode)
        return self.nodes[theNode]

    def getNode(self, theNode):
        if theNode in self.nodes.values():
            return self.nodes[theNode]
        
    def addEdges(self, fromNode, toNode, theWeight = 0):
        if fromNode not in self.nodes:
            self.addNode(fromNode)
        if toNode not in self.nodes:
            self.addNode(toNode)
        self.nodes[fromNode].addNeighbour(self.nodes[toNode], theWeight)
        self.nodes[toNode].addNeighbour(self.nodes[fromNode], theWeight)

    def getNodes(self):
        return self.nodes.keys()

if __name__ == '__main__':
    graph = Graph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addNode('E')
    graph.addNode('F')
    graph.addNode('G')
    graph.addEdges('A', 'B', 1)
    graph.addEdges('C', 'A', 2)
    graph.addEdges('B', 'D', 3)
    graph.addEdges('D', 'C', 4)
    graph.addEdges('C', 'E', 5)
    graph.addEdges('E', 'F', 6)
    graph.addEdges('G', 'F', 7)