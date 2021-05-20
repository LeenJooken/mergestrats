import FileNodeExpansionPack
import numbers

class GraphExpansionPack:

    def __init__(self,baseGraph):
        self.baseGraph = baseGraph
        self.fileNodeExpansion = FileNodeExpansionPack.FileNodeExpansionPack(baseGraph.getNodeIterator(),baseGraph.getNodesList(),baseGraph.getClusterNodesList())

    #expand the base graph with file nodes that give a notion of the isolated files a programmer works on
    #@return a dictionary with the file nodes and edges lists in respectively "nodes" and "edges"
    def expandWithFileNodes(self):
        newNodeIterator = self.fileNodeExpansion.createFileNodes()
        if(isinstance(newNodeIterator,numbers.Number)):
            self.baseGraph.setNodeIterator(newNodeIterator)

        fileNodesList = self.fileNodeExpansion.getNodesList()
        print("De file ")
        for node in fileNodesList:
            print(node.getProgrammerLabel(),": ", node.getLabel()," files weight = ", node.getWeight())

        fileEdgesList = self.fileNodeExpansion.getEdgesList()

        clusterFileNodesList = self.fileNodeExpansion.getClusterNodesList()
        print("De cluster file nodes:")
        for node in clusterFileNodesList:
            print(node.getProgrammerLabel(),": ", node.getLabel()," files   weight = ", node.getWeight())

        clusterFileEdgesList = self.fileNodeExpansion.getClusterEdgesList()

        return {"nodes":fileNodesList,"edges":fileEdgesList,"clusternodes": clusterFileNodesList,"clusteredges":clusterFileEdgesList}
