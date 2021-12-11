# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX


# Class for creating a node and it's value
class Node:
    def __init__(self, value, root):
        self.key = value
        self.parent = root
        
        self.left = None
        self.right = None
        self.size = 1

    # returns the nodes size
    def getSize(self):
        return self.size

    # updates the size
    def updateSize(self):       # sums the size of the nodes below it
        temp = 1
        if self.left != None:
            temp += self.left.getSize()

        if self.right != None:
            temp += self.right.getSize()

        self.size = temp
    
    # creates a child 
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node