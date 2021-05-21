import Node
import Programmer
import Edge
import NodeWeightCalculator
import EdgeCalculator
import EdgeWeightCalculator
import GraphSimplification
#class that represents the social graph,
#contains a node and edge list
class Graph:

    #@param listOfProgrammers is a list of Programmer objects
    def __init__(self,listOfProgrammers,listOfCommits,nodeIterator):
        self.nodeslist = []
        self.edgeslist = []
        self.clusterNodeslist = []
        self.clusterEdgeslist = []
        self.nodeIterator = nodeIterator

        self.constructGraph(hihihih,listOfCommits)
