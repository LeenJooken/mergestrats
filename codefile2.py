class FileNode:

    def __init__(self,id,node):
        #unique node ID
        self.ID = id
        #the base grpah node this file node is connected to
        self.baseGraphNode = node
        #the programmer this baseGraphNode contains and thus this file node is connected to
        self.programmer = node.getProgrammer()
        #distinct list of files this programmer worked on and did NOT pair program on!
        self.distinctFileList = self.buildDistinctFileList()
        #copy by value
        self.isolatedFileList = self.distinctFileList[:]
        self.collaborationths = 3


        #construct the list of files this programmer worked on alone
        self.constructIsolatedFileList()

        #weight of the file node
        self.weight = self.calculateWeight()

    def getID(self):
        return self.ID

    def getWeight(self):
        return self.weight

    def setWeight(self,weight):
        self.weight = weight
